# coding=utf-8
import requests, time, json, configparser, random, os, yagmail

# python2支持
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 模拟包头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# 获取当前的时间
def get_time():
    return time.strftime('%Y%m%d', time.localtime(time.time()))


# 帐号密码信息读取
def getUserInfo():
    try:
        config = configparser.ConfigParser()
        config.read('./info.ini')
        usernames = config['Information']['username'].split(',')
        passwords = config['Information']['password'].split(',')
        emails = config['Information']['email'].split(',')

        print('get userdata success')
        return list(zip(usernames, passwords, emails))

    except Exception as e:
        print('get userdata failed\n %s' % e)
        return None


# 帐号密码信息读取
def getSMTPInfo():
    try:
        config = configparser.ConfigParser()
        config.read('./info.ini')
        user = config['SMTP']['user']
        password = config['SMTP']['password']
        host = config['SMTP']['host']

        print('get SMTP info success')
        return user, password, host

    except Exception as e:
        print('get userdata failed\n %s' % e)
        return None


# 登录并获取old_info
def login(userdata):
    login_url = "https://app.upc.edu.cn/uc/wap/login/check"
    session = requests.session()
    response = session.post(login_url, headers=headers, data=userdata, timeout=20)
    response.encoding = "UTF-8"
    # print(response.text,'\n')
    info_url = "https://app.upc.edu.cn/ncov/wap/default/index"
    html_info = session.get(info_url, headers=headers, timeout=20)
    html_info.encoding = "UTF-8"
    return session, html_info.text


def save_info(session, info):
    save_url = "https://app.upc.edu.cn/ncov/wap/default/save"
    save_response = session.post(url=save_url, data=info, headers=headers, timeout=20)
    save_response.encoding = "UTF-8"
    return save_response.text


def send_email(status, info, email_address):
    try:
        user, password, host = getSMTPInfo()
        yagmail_server = yagmail.SMTP(user=user, password=password, host=host)
        email_name = [email_address]
        email_title = [status]
        email_content = [info]
        yagmail_server.send(to=email_name, subject=email_title, contents=email_content)
        yagmail_server.close()
        print("email finished")
    except Exception as e:
        print(e)


def process(userdata, email_address):
    # 登录返回old_info
    session, html = login(userdata)
    # print(html)
    old_info = json.loads(html)['d']['oldInfo']

    # 获取当前日期
    today_date = get_time()

    # 重构old_info
    old_info['date'] = today_date
    # print(old_info)

    # 提交信息，对应的接口为save
    save_res = save_info(session, old_info)
    print('签到结果:' + json.loads(save_res)['m'])
    session.close()

    if email_address:
        # 结束后发送邮件
        if json.loads(save_res)['m'] == '操作成功':
            send_email("[签到成功] Covid-19中国石油大学(华东)疫情防控自动化填报",
                       user[0] + " " + time.strftime('%Y.%m.%d', time.localtime(time.time())) + " " + '签到结果:' + json.loads(save_res)['m'],
                       email_address)
        else:
            send_email("[签到失败] Covid-19中国石油大学(华东)疫情防控自动化填报",
                       user[0] + " " + time.strftime('%Y.%m.%d', time.localtime(time.time())) + " " + '签到结果:' + json.loads(save_res)['m'],
                       email_address)


if __name__ == "__main__":
    # 获取用户信息
    userinfos = getUserInfo()
    # print(userinfos)

    for user in userinfos:
        print('账号:' + user[0] + ' 密码:' + user[0] + ' 邮箱:' + user[2])
        user_data = {
            'username': user[0],
            'password': user[1]
        }
        # print(user_data)
        process(user_data, user[2])
