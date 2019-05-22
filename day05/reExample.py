#!/usr/bin/env python
#-*- coding:utf8 -*-

import re
print(re.findall(r'(\d+)-([a-z])','34324-dfsdfs777-hhh')) 　　　　　　 # [('34324', 'd'), ('777', 'h')]
  
print(re.search(r'(\d+)-([a-z])','34324-dfsdfs777-hhh').group(0))    # 34324-d 返回整体
print(re.search(r'(\d+)-([a-z])','34324-dfsdfs777-hhh').group(1))    # 34324 获取第一个组
print(re.search(r'(\d+)-([a-z])','34324-dfsdfs777-hhh').group(2))    # d 获取第二个组
print(re.search(r'(\d+)-([a-z])','34324-dfsdfs777-hhh').group(3))    # IndexError: no such group
  
print(re.search(r"(jason)kk\1","xjasonkkjason").group())  　　　　　　 #\1表示应用编号为1的组 jasonkkjason
  
print(re.search(r'(\d)gg\1','2j333gg3jjj8').group())                 # 3gg3 \1表示使用第一个组\d
  
# 下面的返回None 为什么是空？而匹配不到3gg7，因为\1的不仅表示第一组，而且匹配到的内容也要和第一组匹配到的内容相同，第一组匹配到3，第二组匹配到7 不相同所以返回空
print(re.search(r'(\d)gg\1','2j333gg7jjj8'))
  
print(re.search(r'(?P<first>\d)abc(?P=first)','1abc1'))              # 1abc1 声明一个组名，使用祖名引用一个组　
  
r=re.match('(?P<n1>h)(?P<n2>\w+)','hello,hi,help')　　# 组名的另外一种用法
print(r.group())                       　　　　　　　　 # hello 返回匹配到的值
print(r.groups())                      　　　　　　　　 # ('h', 'ello')返回匹配到的分组
print(r.groupdict())                   　　　　　　　　 # {'n2': 'ello', 'n1': 'h'} 返回分组的结果，并且和相应的组名组成一个字典
  
# 分组是从已经匹配到的里面去取值
origin ="hello alex,acd,alex"
print(re.findall(r'(a)(\w+)(x)',origin))                  # [('a', 'le', 'x'), ('a', 'le', 'x')]
print(re.findall(r'a\w+',origin))                         # ['alex', 'acd', 'alex']
print(re.findall(r'a(\w+)',origin))                       # ['lex', 'cd', 'lex']
print(re.findall(r'(a\w+)',origin))                       # ['alex', 'acd', 'alex']
print(re.findall(r'(a)(\w+(e))(x)',origin))               # [('a', 'le', 'e', 'x'), ('a', 'le', 'e', 'x')]
  
r=re.finditer(r'(a)(\w+(e))(?P<name>x)',origin)
for i in r :
    print(i,i.group(),i.groupdict())
'''
    [('a', 'le', 'e', 'x'), ('a', 'le', 'e', 'x')]
    <_sre.SRE_Match object; span=(6, 10), match='alex'> alex {'name': 'x'}
    <_sre.SRE_Match object; span=(15, 19), match='alex'> alex {'name': 'x'}
'''
  
print(re.findall('(\w)*','alex'))                   # 匹配到了alex、但是4次只取最后一次即 x 真实括号只有1个
print(re.findall(r'(\w)(\w)(\w)(\w)','alex'))       # [('a', 'l', 'e', 'x')]  括号出现了4次，所以4个值都取到了
  
origin='hello alex sss hhh kkk'
print(re.split(r'a(\w+)',origin))                   # ['hello ', 'lex', ' sss hhh kkk']
print(re.split(r'a\w+',origin))                     # ['hello ', ' sss hhh kkk']
