#!/usr/bin/env python
# -*- coding:utf8 -*-
# 几个读写文件的例子 

#读取一个文件中的10行写入另外一个文件中
with open('/etc/passwd','rb') as f1,open('passwd2','wb') as f2:
    times = 0
    for line in f1:
        times += 1
        if times <= 10:
            f2.write(line)
        else:
            break

#将一个文件一行一行读取并批量替换并写入另外一个文件
with open('passwd2','rb') as f1,open('passwd3','wb') as f2:
    for line in f1:
        new_str = line.replace('root','ROOT')
        f2.write(new_str)

#假设现在有这样一个需求，有一个10G大的文件，如何拷贝到另一个文件中去？
#下面将讲一下如何同时打开两个文件进行处理，以及文件太大的时候如何读取用with语句就可以同时打开两个文件，一个读，一个写。
#假设1.txt文件有10G大，如果用read则一次性就将内容读到内存中去了，这显然不合适，如果用readline()的话虽然也可以读一行，
#但是并不知道何时结束，但是可以用for循环读取文件这个可迭代的对象，一行行的读取。下面三行代码就可以实现了
with open('/etc/passwd','rb',encoding='utf-8') as fread,open('passwd4.txt','wb') as fwrite:
    for line in fread:　　　　　　　　　　#一行行的读
        fwrite.write(line)　　　　　　　  #一行行的写
