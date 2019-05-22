#!/usr/bin/env python
#-*- coding:utf-8 -*-

#示例：使用yield函数生成器，能够用next()调用或for循环使用
def genNum(x):
    y = 0
    while y <= x:
        yield y
        y += 1

g1 = genNum(5)

for i in g1:
    print(i)

#示例：求1到10的平方，可以使用列表解析或者生成器，也可以是用yield
def genNum1(n):
    i = 1
    while i <= 10:
        yield i ** 2
        i += 1
        
g2 = genNum1(5)

for i in g2:
    print(i)
