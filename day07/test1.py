#!/usr/bin/env python
#-*- coding:utf-8 -*-
import yaml

if __name__ == '__main__':
    guy = {
        'name': '陈二',
        'age': '22',
        'tag': 'loser'
    }

    # 直接dump可以把对象转为YAML文档
    print(yaml.dump(guy))

    # 也可以直接dump到文件或者流中
    with open('guy.yaml', 'w', encoding='UTF-8') as guy_file:
        yaml.dump(guy, guy_file)

