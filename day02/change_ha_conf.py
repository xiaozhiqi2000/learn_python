#!/usr/bin/env python
# -*- coding:utf-8 -*-
#对ha.conf进行增删查

def ha_fetch(backend_domain):
    """
    获取ha.conf的backend有哪些后端server
    :param backend_domain: 后端域名
    :return:
    """

    result = []

    with open("ha.conf", 'r', encoding='utf-8') as f:
        flag = False
        for line in f:
            # 当以backend开头且backend backend_domain等于用户输入的backend backend_domain,进入下一轮循环
            if line.strip().startswith("backend") and line.strip() == "backend " + backend_domain:
                flag = True
                continue
            # 当flag=True且以backend开头的时候跳出循环了
            if flag and line.strip().startswith("backend"):
                flag = False
                break
            # 只有当flag=True且没有空行的时候才写入result列表中,这样就获取到backend_domain对应的server记录了
            if flag and line.strip():
                result.append(line.strip())

    return result


def ha_add(backend_domain, record):
    """

    :param backend_domain:
    :param record: {"backend":"www.oldboy.org","record":{"server":"192.168.1.9","weight":"30","maxconn":"20"}}
    :return:
    """

    record_list = ha_fetch(backend_domain)
    if not record_list:
        with open('ha.conf', 'r') as old, open('ha_new.conf', 'w') as new:
            for line in old:
                new.write(line)

            new.write("\nbackend " + backend_domain + "\n")
            new.write(" " * 8 + record + "\n")
    else:
        if record in record_list:
            import shutil
            shutil.copy("ha.conf", "new.conf")
        else:
            record_list.append(record)
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend_domain:
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


def ha_add2(backend_domain, record):
    """

    :param backend_domain:
    :param record:
    :return:
    """
    with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
        in_backend = False
        has_backend = False
        has_record = False
        for line in old:
            if line.strip().startswith('backend') and line.strip() == "backend " + backend_domain:
                has_backend = True
                in_backend = True
                new.write(line)
                continue

            if in_backend and line.strip().startswith('backend'):
                if not has_record:
                    new.write(" " * 8 + record + '\n')
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
            new.write('backend ' + backend_domain + '\n')
            new.write(' ' * 8 + record + '\n')


def ha_delete(backend_domain, record):
    """

    :param backend:
    :param record:
    :return:
    """
    pass


HA_LIST = ["查看ha记录", "添加ha记录", "删除ha记录", "退出"]

while True:
    for i, k in enumerate(HA_LIST, 1):
        print(i, k)
    choice_num = input("请选择您的操作:>>>")
    choice_num = int(choice_num)

    if choice_num == 1:
        backend = input("enter backend>>>")
        ret = ha_fetch(backend)
        if ret:
            print(ret)
        else:
            print("no record")
            continue
    if choice_num == 2:
        record_json = input("enter backend and record>>>")

        import json
        result = json.loads(record_json)

        backend_domain = result['backend']
        record = "server " + result['record']['server'] + " " + result['record']['server'] + " " +\
                 "weight " + result['record']['weight'] + " " +\
                 "maxconn " + result['record']['maxconn']

        ha_add(backend_domain, record)
    if choice_num == 3:
        record_json = input("enter backend and record>>>")

        import json
        result = json.loads(record_json)

        backend_domain = result['backend']
        record = "server " + result['record']['server'] + result['record']['server'] + \
                 "weight" + result['record']['weight'] + \
                 "maxconn " + result['record']['maxconn']

        ha_delete(backend_domain, record)
    if choice_num == 4:
        break
