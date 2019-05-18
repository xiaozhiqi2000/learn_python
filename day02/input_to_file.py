#!/usr/bin/env python
# -*- coding:utf8 -*-

#判断文件是否存在，存在则打开,让用户通过键盘反复输入多行数据,追加保存至此文件中

import os
import os.path

filename = 'user_input.txt'

if os.path.isfile(filename):
    f1 = open(filename,'a+')
else:
    f1 = open(filename,'w+')


while True:
    line = input('Enter somethin> ')
    if line == 'q' or line == 'quit':
        break
    f1.write(line + '\n')

f1.close()
