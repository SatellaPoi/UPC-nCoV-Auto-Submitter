# UPC-nCoV-Auto-Submitter
中国石油大学（华东）疫情防控通自动填报python版本
由Satella_Poi优化并修改

## 说明
**现公益为大家提供打卡服务，如有需要请联系QQ：122602310

**本人不对因为滥用此程序造成的后果负责，请在合理且合法的范围内使用本程序。**

**本程序仅供研究交流使用，如果填报表中任意情况发生变化，比如地点发生变化，请务必在程序运行之前手动打卡。**

## 依赖库
```
requests
configparser
yagmail 
```

## 运行方法
1. 安装依赖库
2. 修改`info.ini`为自己的信息，`[Information]`中修改自己的账号，密码，邮件(可选，打卡完成邮件提醒),支持多账号打卡，填写时`,`隔开，`[SMTP]`处修改为自己的SMTP信息
3. 执行` python main.py `即可完成自动填报

## 简易web页面部署

1. 部署LNMP环境
2. 安装Fastadmin面板
3. 使用Fastadmin提供的CURD生成

```
php think crud -t user_tbl -c account/Account
php think menu -c account/Account
```

## 服务器定时任务

0 7 * * * root /your/path/to/python /your/path/to/main.py
每天早上7点执行脚本

## TODO
- [x] 基本功能
- [x] 邮件提醒
- [x] 数据库支持
- [x] web页面支持

## History
- 2020/12/08 基本功能和邮件功能实现
- 2021/03/02 web页面和数据库支持实现 
