#!/usr/bin/env python
# -*-coding: utf8-*-
"""
用户管理程序
    普通用户：登录，注册，修改密码，查看本用户信息
    管理员用户：登录，注册，修改密码，查看本用户信息
              删除，添加普通用户
              修改普通用户密码
              查看所有普通用户，按照指定关键字搜索用户信息
              提高普通用户权限
    1. 用户信息：存文件n
    2. 权限使用装饰器
"""

USER_FLAG = {"is_login": False}


def str_to_num(arg):
    try:
        ret = int(arg)
        return ret
    except:
        return False


def inputData():
    username = input("请输入用户名:")
    password = input("请输入密  码:")
    return username, password


def checkUser(user):
    with open("userinfo", "r") as f:
        for line in f:
            userdata = line.strip().split("|")[0]
            if userdata == user:
                return False


def checkAdmin(func):
    def inner(*args, **kwargs):
        if USER_FLAG.get('userType', None) == '2':
            ret = func(*args, **kwargs)
            return ret
        else:
            print("无权限查看")
    return inner

def checkLogin(func):
    def inner():
        if USER_FLAG.get('is_login', None):
            ret = func()
            return ret
        else:
            print("请先登录,然后才能继续操作")
    return inner

@checkLogin
@checkAdmin
def seeUserInfo():
    with open("userinfo", "r") as f:
        for line in f:
            user = line.strip().split("|")
            return user



def login(user, pwd):
    with open("userinfo", "r", encoding="utf8") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == user and data[1] == pwd:
                USER_FLAG['is_login'] = True
                USER_FLAG['current'] = user
                USER_FLAG['userType'] = data[4]
                return True
            else:
                return False


def register(*args):
    print(args)
    ret = checkUser(args[0])
    if ret == False:
        print("注册失败,用户已经存在")

    else:
        with open("userinfo", "r+", encoding="utf8") as f:
            f.write(args[0] + "|" + args[1] + "|" + args[2] + "|" + args[3] + "|" + args[4])
            return True


@checkLogin
def changepwd():
    import os
    newPassword = input("请输入你的新密码:")
    file_tmp = open(r'file_tmp', 'x')
    login_file = 'userinfo'
    with open(r'userinfo') as file:
        for i in file:
            i = i.strip().split("|")
            li = []
            if i[0] == USER_FLAG['current']:
                i[1] = newPassword
                li.append(i[0])
                li.append(i[1])
                li.append(i[2])
                li.append(i[3])
                li.append(i[4])
            else:
                li = [i[0], i[1], i[2], i[3], i[4]]
            file_tmp.write("|".join(li)+'\n')
            file_tmp.close()
    os.remove(login_file)
    os.rename('file_tmp', login_file)
    print("修改密码成功")


@checkLogin
def searchUser():
    pass


@checkLogin
def searchSomthing():
    pass


def nextData():
    nextnum = input("请继续输入：1.修改密码 2.查询用户信息 3.模糊查询 4.退出>>>")
    return nextnum

def nextDo():
    while True:
        nextnum = nextData()
        nextnum = str_to_num(nextnum)
        if nextnum == 1:
            changepwd()
        elif nextnum == 2:
            info = seeUserInfo()
            if info:
                print("="*100)
                print(info)
                print("="*100)
                continue
        elif nextnum == 3:
            pass
        elif nextnum == 4:
            break
        else:
            print("请输入有效数字")



while True:
    num = input("1.登录，2.注册，3.修改密码，4.查询用户信息 5.模糊查询：")
    num = str_to_num(num)
    if num == 1:
        username, password = inputData()
        ret = login(username, password)
        if ret:
            print("登录成功")
            nextDo()
        else:
            print("用户名不存在或者密码错误：请重新登录或者注册")
    elif num == 2:
        username, password = inputData()
        emailAdd = input("请输入你的邮箱:")
        phoneNum = input("请输入你的电话:")
        userType = input("请输入你的用户类型1.普通用户 2.管理员用户:")

        ret = register(username, password, emailAdd, phoneNum, userType)
        if ret:
            print("注册成功")
    elif num == 3:
        changepwd()
    elif num == 4:
        searchUser()
    elif num == 5:
        searchSomthing()
    else:
        print("请输入有效数字")

