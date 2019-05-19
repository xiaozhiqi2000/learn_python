#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fetch(backend):
    result = []
    with open("ha.conf", 'r', encoding='utf-8') as f:
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend"):
                flag = False
                break
            if flag and line.strip():
                result.append(line.strip())

    return result


def add(backend, record):
    record_list = fetch(backend)
    if not record_list:
        with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
            for line in old:
                new.write(line)

            new.write("\nbackend " + backend + "\n")
            new.write(" " * 8 + record + "\n")
    else:
        if record in record_list:
            pass
            # import shutil
            # shutil.copy("ha.conf", "new.conf")
        else:
            record_list.append(record)
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                    if flag and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                        continue
                    if line.strip() and not flag:
                        new.write(line)


def add2(backend, record):
    with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
        in_backend = False
        has_backend = False
        has_record = False
        for line in old:
            if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                has_backend = True
                in_backend = True
                new.write(line)
                continue
 
            if in_backend and line.strip().startswith('backend'):
                if not has_record:
                    new.write(" "*8 + record + '\n')
                new.write(line)
                in_backend = False
                continue
 
            if in_backend and line.strip() == record:
                has_record = True
                new.write(line)
                continue
 
            if line.strip():
                new.write(line)
 
        if not has_backend:
            # 写backend，写record
            new.write('backend '+ backend + '\n')
            new.write(' '*8 + record + '\n')

def delete(backend, record):
    pass

l = ["查看ha记录", "添加ha记录", "删除ha记录", "退出"]

while True:
    for i,k in enumerate(l,1):
        print(i,k)
    choice_num = input("请选择您的操作:>>>")
    choice_num = int(choice_num)

    if choice_num == 1:
        backend = input("enter backend>>>")
        ret = fetch(backend)
        if ret:
            print(ret)
        else:
            print("no record")
            continue
    if choice_num == 2:
        backend = input("enter backend>>>")
        record = input("enter record>>>")
    if choice_num == 3:
        backend = input("enter backend>>>")
        record = input("enter record>>>")
    if choice_num == 4:
        break







