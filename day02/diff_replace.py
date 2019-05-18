#!/usr/bin/env python
# -*- encoding:utf8 -*-
# 数据库已有的数据，通过集合的方法将新数据更新到数据库中

# 数据库中原有
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}
# cmdb 新汇报的数据
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}
old_set=set(old_dict)
new_set=set(new_dict)
 
del_set=old_set.difference(new_set)
add_set=new_set.difference(old_set)
flush_set=old_set.intersection(new_set)
 
for i in del_set:
    old_dict.pop(i)
 
for i in add_set:
    old_dict[i]=new_dict[i]
 
for i in flush_set:
    old_dict[i] = new_dict[i]
print(old_dict)
