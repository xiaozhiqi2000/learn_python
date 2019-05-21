#!/usr/bin/env python
# -*-coding:utf-8-*-
# 生成随机数验证码

import random

li = []
for i in range(6):
    r = random.randrange(0, 6)
    if r == 2 or r == 4:
        temp = random.randrange(0, 9)
        li.append(str(temp))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)


randNum = "".join(li)
print(randNum)
