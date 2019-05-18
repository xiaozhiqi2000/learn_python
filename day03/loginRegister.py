#!/usr/bin/env python
# -*- coding:utf8 -*-
# 这是一个用户登录注册的函数式编程

def str_to_num(arg):
    """
    这个函数是将字符串转为数字
    :param arg:
    :return:
    """
    try:
        ret = int(arg)
        return ret
    except:
        return False


def datainput():
    """
    用于用户输入的账号密码
    :return: 返回账号密码
    """
    userdata = []
    username = input("input your username:")
    password = input("input your password:")
    userdata.append(username)
    userdata.append(password)
    return userdata


def login(*args):
    """
    从文件中读取用户的账号密码
    :param args: 用户的账号密码
    :return:
    """
    f = open('db', 'r')
    for line in f:
        data = line.strip().split('|')
        if data[0] == args[0] and data[1] == args[1]:
            return True
    return False


def register(*args):
    """
    先从文件检验是否有该用户，没有就将用户填写用户名写入文件
    :param args: 用户的账号密码
    :return: 
    """
    f = open('db', 'r')
    for line in f:
        user = line.strip().split('|')

        if args[0] in user:
            return False
    else:
        f = open('db', 'a')
        userdata = "\n" + args[0] + "|" + args[1]        
        f.write(userdata)
        f.close()
        return True


def main():
    num = input("1.登录，2.注册：")
    result = str_to_num(num)
    if result:
        if int(num) == 1:
            data = datainput()
 
            result = login(*data)
            if result:
                print('登录成功')
            else:
                print('登录失败')
        elif int(num) == 2:
            data = datainput()
            ret = register(*data)
            if ret:
                print("注册成功")
            else:
                print("注册失败,用户已存在")
        else:
            print("你输入的不存在！")
    else:
        print("请输入数字")


main()



