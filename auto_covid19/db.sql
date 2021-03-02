CREATE TABLE IF NOT EXISTS `user_tbl`(
   `user_id` INT UNSIGNED AUTO_INCREMENT,
   `username` VARCHAR(10) NOT NULL,
   `password` VARCHAR(40) NOT NULL,
   `email` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `user_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into user_tbl (username, password, email)
values ('*****','***','***@');
