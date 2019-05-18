#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 检测用户登录用到了while/fi语句

import getpass

name = 'tom'
pwd = 123456
count = 0

while True:
    if count < 3:
        print("Please enter your name and password !")
        username = input("username:")
        password = getpass.getpass("password:")

        if username == name and password == pwd:
            print("恭喜你登陆成功！")
            break
        else:
            print("登陆失败！用户名或者密码错误")
    else:
        print("你已经输错3次,正在退出....")
        break

    count += 1
