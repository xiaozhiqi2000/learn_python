#!/usr/bin/env python
# -*- coding:utf8 -*-

#示例1：        
l = [1,2,3,4,5]
l1 = [ x ** 2 for x in l if x >= 3 ]
print(l1)
    
#示例2：        
l2 = [ (i ** 2)/2 for i in range(1,11) ]
print(l2)
    
#示例3：        
import os

filelist1 = os.listdir('/var/log/')
s1 = 'hello.log'
s1.endswith('.log')

s2 = 'hello'
s2.endswith('.log')

filelist2 = [ i for i in filelist1 if i.endswith('.log') ]
print(filelist2)

filelist3 = [ i for i in os.listdir('/var/log/') if i.endswith('.log') ]
print(filelist3)
    
#示例4：        
l3 = ['x','y','z']
l4 = [1,2,3]
l5 = [ (i,j) for i in l3 for j in l4 ]

print(l5)
    
#示例5：            
l6 = ['x','y','z']
l7 = [1,2,3]
l8 = [ (i,j) for i in l6 for j in l7 if j != 1 ]

print(l8)
