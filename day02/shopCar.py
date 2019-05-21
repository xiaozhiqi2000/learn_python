#!/usr/bin/evn python
#-*-coding:utf-8-*-

product = [
    ("iphone",5800),
    ("watch",380),
    ("bike",800),
    ("book",120),
    ("computer",4000)
]
 
shopping_car = []
 
salary = input("input your salary: ")
if salary.isdigit():
    salary = int(salary)
    while True:
        for i in enumerate(product):
            print(i)
 
        user_choice = input(">>>或者q:")
 
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 0 and user_choice < len(product):
                p_item = product[user_choice]
                if salary >= p_item[1]:
                    shopping_car.append(p_item[0])
                    salary -= p_item[1]
                    print("你购买了\033[32m%s\033[0m,你的余额剩余\033[31m%s\033[0m" % (p_item[0], salary))
                else:
                    print("\033[31m你的余额不足\033[0m")
            else:
                print("你输入的项目[%s]不存在,请重新输入" % user_choice)
        elif user_choice == 'q':
            print("你购买了这些商品:".center(30,"-"))
            for i in shopping_car:
                print("\033[32m%s\033[0m" %i)
            print("\033[31m余额%s\033[0m" %salary)
            exit()
        else:
            print("你输入的[%s]不存在" % user_choice)
else:
    print("你输入的金额不正确！请重新输入金额！")
