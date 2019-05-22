#!/usr/bin/env python
#coding:utf8

import configparser

config = configparser.ConfigParser()
config.read('xxoo.conf', encoding='utf-8')
ret = config.sections()          #获取所有节点　　
ret1 = config.items('section1')   #获取指定节点下所有的键值对
ret2 = config.options('section1') #获取指定节点下所有的建
ret3 = config.get('section1', 'k1') #获取指定节点下指定key的值
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print("ret>>>",ret)
print("ret1>>>",ret1)
print("ret2>>>",ret2)
print("ret3>>>",ret3)

#### 2. 检查、删除、添加节点
# 检查节点
has_sec = config.has_section('section1')
print(has_sec)
 
# 添加节点
config.add_section("SEC_1")
config.write(open('xxoo.conf', 'w'))
  
#设置指定组内的键值对
config.set('SEC_1', 'k10', "123")
config.write(open('xxoo.conf', 'w'))

# 删除节点
config.remove_section("SEC_1")
config.write(open('xxoo.conf', 'w'))

