# 今天主要内容
1. [python模块]()
2. [正则表达式re模块]()

## Python模块

用一砣代码实现了某个功能的代码集合。 类似于函数式编程和面向过程编程，函数式编程则完成一个功能，其他代码用来调用即可，提供了代码的重用性和代码间的耦合。而对于一个复杂的功能来，可能需要多个函数才能完成（函数又可以在不同的.py文件中），n个 .py 文件组成的代码集合就称为模块。模块分为内建模块、自定义的模块、安装的第三方的模块

### 1. 导入模块

Python之所以应用越来越广泛，在一定程度上也依赖于其为程序员提供了大量的模块以供使用，如果想要使用模块，则需要导入。导入模块有一下几种方法：
```
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename
from module.xx.xx import *

导入模块其实就是告诉Python解释器去解释那个py文件
导入一个py文件，解释器解释该py文件
导入一个包，解释器解释该包下的 __init__.py 文件
```

那么问题来了，导入模块时是根据那个路径作为基准来进行的呢？即：sys.path
```
import sys
print(sys.path)
['', '/home/tomcat/.pyenv/versions/3.5.1/lib/python35.zip',
'/home/tomcat/.pyenv/versions/3.5.1/lib/python3.5',
'/home/tomcat/.pyenv/versions/3.5.1/lib/python3.5/plat-linux',
'/home/tomcat/.pyenv/versions/3.5.1/lib/python3.5/lib-dynload',
'/home/tomcat/.pyenv/versions/3.5.1/lib/python3.5/site-packages']
```

如果sys.path路径列表没有你想要的路径，可以通过 sys.path.append('路径') 添加。
```
import sys
import os

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
```
## 正则表达式re模块

正则表达式使用单个字符串来描述、匹配一系列符合某个句法规则的字符串，在文本处理方面功能非常强大，也经常用作爬虫，来爬取特定内容，Python本身不支持正则，但是通过导入re模块，Python也能用正则表达式，下面就来讲一下python正则表达式的用法。正则表达式默认以单行开始匹配的

### 1.匹配规则

![avatar](/day05/imgs/regularexpress.png)

### 2.re模块相关方法
```
re.findall()  可以将匹配到的结果以列表的形式返回，如果匹配不到则返回一个空列表，下面来看一下代码中的使用
re.finditer() 可以将匹配到的结果生成一个迭代器
re.search()   是匹配整个字符串直道匹配到一个就返回
re.match()    从要匹配的字符串的开头开始，尝试匹配，如果字符串开始不符合正则表达式，则匹配失败，函数返回None,匹配成功的话用group取出匹配的结果
re.split()    能够将匹配的子串分割后返回列表
re.sub()      能将匹配到的字段用另一个字符串替换返回替换后的字符串
re.subn()     能将匹配到的字段用另一个字符串替换返回替换后的字符串，subn还返回替换的次数
```
- re.findall()  可以将匹配到的结果以列表的形式返回，如果匹配不到则返回一个空列表，下面来看一下代码中的使用
   ```
   import re
   
   def re_method():
       s1 = 'Hello, this is Joey'
       s2 = 'The first price is $9.90 and the second price is $100'
       print(re.findall(r'\w+',s1))
       print(re.findall(r'\d+\.?\d*',s2))
    
   if __name__ == '__main__':
       re_method()
   ```

- re.finditer() 可以将匹配到的结果生成一个迭代器
   ```
   import re
    
   def re_method4():
       # finditer
       s2 = 'The first price is $9.90 and the second price is $100'
       i = re.finditer(r'\d+\.?\d*',s2)
       for m in i:
           print(m.group())
    
   if __name__ == '__main__':
       re_method4()
   ```

- re.search() 是匹配整个字符串直道匹配到一个就返回
   ```
   import re
    
   def re_demo():
       txt = 'If you puchase more than 100 sets, the price of product A is $9.90.'
       m = re.search(r'(\d+).*\$(\d+\.?\d*)',txt)
       print(m.groups())
    
   if __name__ == '__main__':
       re_demo()
   ```
   
- re.match() 从要匹配的字符串的开头开始，尝试匹配，如果字符串开始不符合正则表达式，则匹配失败，函数返回None,匹配成功的话用group取出匹配的结果
   ```
   import re
    
   def re_method():
       # search vs match
       s = 'abcdc'
       print(re.search(r'c',s))  #search是从开头到结尾的匹配到第一个匹配的
       print(re.search(r'^c', s))
       print(re.match(r'c',s))   #match是开头开始匹配
       print(re.match(r'.*c', s))
    
   def re_match_object():
       # match对象
       s1 = 'Joey Huang'
       m = re.match(r'(\w+) (\w+)',s1)
       print(m.group(0,1,2))
       print(m.groups())
    
       m1 = re.match(r'\w+ (\w+)', s1)
       print(m1.group(1))
       print(m1.groups())
    
    
   if __name__ == '__main__':
       re_method()
       re_match_object()
   ```
   
- re.split() 能够将匹配的子串分割后返回列表
   ```
   import re
    
   def re_method1():
       # split
       s = 'This is Joey Huang'
       print(re.split(r'\W', s))
    
   if __name__ == '__main__':
       re.method1()
   ```
   
- re.sub、re.subn() 能将匹配到的字段用另一个字符串替换返回替换后的字符串，subn还返回替换的次数
   ```
   import re
    
   def re_method2():
       # sub
       s2 = 'The first price is $9.90 and the second price is $100'
       print(re.sub(r'\d+\.?\d*','<number>',s2,2)) # 还能指定替换的次数
    
   def re_method3():
       # subn
       s2 = 'The first price is $9.90 and the second price is $100'
       print(re.subn(r'\d+\.?\d*','<price>',s2))
    
   if __name__ == '__main__':
       re_method2()
       re_method3()
   ```

### 3.re模块flags标识位
```
re.DOTALL
re.MULTILINE
?非贪婪模式
re.I/re.IGNORECASE
re.VERBOSE
```
- re.DOTALL
   ```
   正则表达式默认以单行开始匹配的
   
   import re
    
   def re_pattern_syntax():
       # .表示任意单一字符
       # *表示前一个字符出现>=0次
       # re.DOTALL就可以匹配换行符\n,默认是以行来匹配的
       print(re.match(r'.*', 'abc\nedf').group())
       print('*' * 80)
       print(re.match(r'.*', 'abc\nedf',re.DOTALL).group())
    
   if __name__ == '__main__':
       re_pattern_syntax()
   ```    
- re.MULTILINE　　
   ```
   正则表达式默认以单行开始匹配的
   
   import re
    
   def re_pattern_syntax1():
       # ^表示字符串开头(单行)
       # re.MULTILINE多行匹配字符串开头
       print(re.findall(r'^abc', 'abc\nedf'))
       print('*' * 80)
       print(re.findall(r'^abc', 'abc\nabc',re.MULTILINE))
    
   def re_pattern_syntax2():
       # $表示字符串结尾
       # re.MULTILINE表示行的结束
       print(re.findall(r'abc\d$', 'abc1\nabc2'))
       print('*' * 80)
       print(re.findall(r'abc\d$', 'abc1\nabc2',re.MULTILINE))
    
   if __name__ == '__main__':
       re_pattern_syntax1()
       re_pattern_syntax2()
   ```    
- ?非贪婪模式　　
   ```
   import re
    
   def re_pattern_syntax4():
       # greedy贪婪/non-greedy非贪婪,默认的是贪婪的匹配
       s = '<H1>title</H1>'
       print(re.match(r'<.+>', s).group())  #贪婪模式会匹配尽量多的匹配
       print(re.match(r'<.+?>', s).group()) #非贪婪模式匹配尽量少的匹配
       print(re.match(r'<(.+)>', s).group(1))
       print(re.match(r'<(.+?)>', s).group(1))
    
   def re_pattern_syntax5():
       # {m}/{m,}/{m,n}
       print(re.match(r'ab{2,4}', 'abbbbbbb').group())  #贪婪模式尽量匹配多
       print(re.match(r'ab{2,4}?', 'abbbbbbb').group()) #非贪婪模式尽量匹配少
       print('*' * 80)
    
   if __name__ == '__main__':
       re_pattern_syntax4()
       re_pattern_syntax5()
   ```    
-re.I/re.IGNORECASE
   ```
   import re
    
   def re_pattern_flags():
       # re.I/re.IGNORECASE
       print(re.match(r'(Name)\s*:\s*(\w+)','NAME : Joey',re.IGNORECASE).groups())
       print('*' * 80)
    
   if __name__ == '__main__':
       re_pattern_syntax_meta_char()
   ```    
- re.VERBOSE
   ```
   import re
    
   def re_pattern_flags1():
       # re.VERBOSE此标识位可以添加注释/re.compile
       s = 'the number is 20.5'
       r = re.compile(r'''
                       \d+   # 整数部分
                       \.?   # 小数点，可能包含也可能不包含
                       \d*   # 小数部分,可选
                       ''',re.VERBOSE)
       print(re.search(r,s).group())
       print(r.search(s).group())
       print('*' * 80)
    
   if __name__ == '__main__':
       re_pattern_syntax_meta_char1()
   ```

### 4.原生字符串、编译、分组
- 原生字符串

   细心的人会发现，我每一次在写匹配规则的话，都在前面加了一个r，为什么要这样写，下面从代码上来说明
   ```
   import re
   #“\b”在ASCII 字符中代表退格键，\b”在正则表达式中代表“匹配一个单词边界”
   print(re.findall("\bblow","jason blow cat"))    #这里\b代表退格键,所以没有匹配到
     
   print(re.findall("\\bblow","jason blow cat"))   #用\转义后这里就匹配到了 ['blow']
     
   print(re.findall(r"\bblow","jason blow cat"))   #用原生字符串后就不需要转义了 ['blow']
   ```
   你可能注意到我们在正则表达式里使用“\d”，没用原始字符串，也没出现什么问题。那是因为ASCII 里没有对应的特殊字符，所以正则表达式编译器能够知道你指的是一个十进制数字。但是我们写代码本着严谨简单的原理，最好是都写成原生字符串的格式
   
- 编译
   
   如果一个匹配规则，我们要使用多次，我们就可以先将其编译，以后就不用每次都在去写匹配规则，下面来看一下用法
   ```
   import re
    
   def re_pattern_flags1():
       # re.VERBOSE此标识位可以添加注释/re.compile
       s = 'the number is 20.5'
       r = re.compile(r'''
                       \d+   # 整数部分
                       \.?   # 小数点，可能包含也可能不包含
                       \d*   # 小数部分,可选
                       ''',re.VERBOSE)
       print(re.search(r,s).group())
       print(r.search(s).group())
       print('*' * 80)
    
   if __name__ == '__main__':
       re_pattern_syntax_meta_char1()
   ```
   
- 分组
   
   除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组，可以有多个组，分组的用法很多，记住正则分组： 去已经匹配到的数据中提取数据

   1. re.match()有无分组比较
   ``` 
   # 无分组
   r = re.match("h\w+", origin)
   print(r.group())     # 获取匹配到的所有结果
   print(r.groups())    # 获取模型中匹配到的分组结果
   print(r.groupdict()) # 获取模型中匹配到的分组结果
    
   # 有分组
   # 为何要有分组？提取匹配成功的指定内容（先匹配成功全部正则，再匹配成功的局部内容提取出来）
    
   r = re.match("h(\w+).*(?P<name>\d)$", origin)
   print(r.group())     # 获取匹配到的所有结果
   print(r.groups())    # 获取模型中匹配到的分组结果
   print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组
   ```
   2. re.search()有无分组比较　　
   ```
   # 无分组
    
   r = re.search("a\w+", origin)
   print(r.group())     # 获取匹配到的所有结果
   print(r.groups())    # 获取模型中匹配到的分组结果
   print(r.groupdict()) # 获取模型中匹配到的分组结果
    
   # 有分组
    
   r = re.search("a(\w+).*(?P<name>\d)$", origin)
   print(r.group())     # 获取匹配到的所有结果
   print(r.groups())    # 获取模型中匹配到的分组结果
   print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组
   ```
   3. re.findall()有无分组比较　　
   ```
   # 无分组
   r = re.findall("a\w+",origin)
   print(r)
    
   # 有分组
   origin = "hello alex bcd abcd lge acd 19"
   r = re.findall("a((\w*)c)(d)", origin)
   print(r)
   ```
   4. re.split()有无分组比较
   ```
   # 无分组
   origin = "hello alex bcd alex lge alex acd 19"
   r = re.split("alex", origin, 1)
   print(r)
    
   # 有分组
    
   origin = "hello alex bcd alex lge alex acd 19"
   r1 = re.split("(alex)", origin, 1)
   print(r1)
   r2 = re.split("(al(ex))", origin, 1)
   print(r2)
   ```
### 常用正则表达式：
[列表解析例子](https://github.com/xiaozhiqi2000/learn_python/blob/master/day04/iterableExample.py)

## 常用正则表达式：
IP：^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$

手机号：^1[3|4|5|8][0-9]\d{8}$

邮箱：[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+

