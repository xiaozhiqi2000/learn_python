#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 猜数字比大小用到了while/fi语句

age = 22
count = 0

for i in range(10):
    if count < 3:
        a = int(input("please input num:"))
        if a == age:
            print("恭喜你,答对了")
            break
        elif a > age:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
    else:
        b = input("你太笨了,这都猜不对,你继续玩吗？(yes or not):")
        if b == 'yes':
            count = 0
            continue
        else:
            print("Bye!下次再玩")

    count += 1
