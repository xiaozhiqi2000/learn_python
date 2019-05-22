#!/usr/bin/env python
#-*- coding:utf-8 -*-
#利用生成器自定义range

def nrange(num):
   temp = -1
   while True:
       temp = temp + 1
       if temp >= num:
           return
       else:
           yield temp

result = nrange(3)
for i in result:
    print(i)
