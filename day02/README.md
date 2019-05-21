# 今天主要内容
1. 数据类型
- [数字](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#数字)
- [字符](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#字符)
- [列表](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#列表)
- [元组](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#元组)
- [集合](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#集合)
- [文件](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#文件)
- [序列操作通用](https://github.com/xiaozhiqi2000/learn_python/tree/master/day02#序列操作通用)

## 数字：int float

python的数字字面量：整数，布尔型，浮点数，复数，所有数字类型均为不可变
- int（整型）
   - 在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647
   - 在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807
- bool(布尔型)
   - 真或假
   - 1 或 0
- float(浮点型)
- 数字操作：+ , -, *, /, //, **, %, -x, +x

## 字符：str 不可变对象

字符串字面量：把文本放入单引号、双引号或三引号中，python2.x默认不是国际字符集unicode，需要unicode定义时加上u,python3无需加
```
str.capitalize()    将字符串的首字母变大写
str.title()         将字符串中的每个单词的首字母大写
str.upper()         将字符串变成大写
str.lower()         将字符串变成小写
str.index()         找出索引对应的字符串
str.find()          同上
str.count()         找出字符串中元素出现的次数
str.format()        也是格式化的一种
str.center()        以什么字符从字符串两边填充
str.join()          以str为分隔符连接字符串
str.split()         以什么为分隔符分隔字符串
str.strip()         将字符串两边中的空格去掉
str.replace()       查找替换
str.isupper()       判断是否为大写
str.islower()       判断是否为小写
str.isalnum()       判断是否是字母数字
str.isalpha()       判断是否是字母下划线
str.isdigit()       判断是否是数字
str.isspace()       判断是否为空
str.startswith()    找出以什么为开头的字符元素
str.endswith()      找出以什么为结尾的字符元素
```

## 列表：list 可变对象
```
list.insert() 在列表中指定索引位置前插入元素
list.append() 在列表尾部插入
list.remove() 删除指定的元素
list.pop() 没有指定索引，则弹出最后一个元素，返回的结果是弹出的索引对应的元素
list.copy() 浅复制,只会复制第一层,如果有嵌套序列则不会复制,如果需要复制则要导入copy模块
list.extend() 把另外一个列表合并，并不是追加
list.index() 列表中元素出现的索引位置
list.count() 统计列表中元素的次数
list.reverse() 进行逆序
list.sort() 进行排序,python3无法把数字和字符串一起排序
l1 + l2 :  合并两个列表，返回一个新的列表，不会修改原列表
l1 * N :   把l1重复N次，返回一个新列表
```

## 元组：tuple 不可变对象
```
tuple.count() 统计元组中元素的个数
tuple.index() 找出元组中元素的索引位置
```

## 字典：dict
```
dict.get(key)      取得某个key的value
dict.has_key(key)  判断字典是否有这个key,在python3中已经废除,使用in 判断
dict.keys()        返回所有的key为一个列表
dict.values()      返回所有的value为一个列表
dict.items()       将字典的键值拆成元组，全部元组组成一个列表
dict.pop(key)      弹出某个key-value
dict.popitem()     随机弹出key-value
dict.clear()       清除字典中所有元素
dict.copy()        字典复制，d2 = d1.copy(),是浅复制,如果深复制需要copy模块
dict.fromkeys(S)   生成一个新字典
dict.update(key)   将一个字典合并到当前字典中
dict.iteritems()   生成key-value迭代器，可以用next()取下个key-value
dict.iterkeys()    生成key迭代器
dict.itervalues()  生成values迭代器

两种遍历字典方法：
第一种：
for k,v in dict.items():
    print(k,v)


第二种：高效
for key in dict:
    print(key,dict[key])
```

## 集合：set 
```
s.add(item)     将item添加到s中。如果item已经在s中，则无任何效果
s.remove(item)  从s中删除item。如果item不是s的成员，则引发KeyError异常
s.discard(item) 从s中删除item.如果item不是s的成员，则无任何效果
s.pop()         随机删除一个任意集合元素，并将其从s删除,如果有变量接收则会接收到删除到的那个元素
s.clear()       删除s中的所有元素
s.copy()        浅复制
s.update(t)     将t中的所有元素添加到s中。t可以是另一个集合、一个序列或者支持迭代的任意对象
s.union(t)        求并集。返回所有在s和t中的元素
s.intersection(t) 求交集。返回所有同时在s和t中的都有的元素
s.intersection_update(t)   计算s与t的交集，并将结果放入s
s.difference(t)            求差集。返回所有在set中，但不在t中的元素
s.difference_update(t)     从s中删除同时也在t中的所有元素
s.symmetric_difference(t)  求对称差集。返回所有s中没有t中的元素和t中没有s中的元素组成的集合
s.sysmmetric_difference_update(t) 计算s与t的对称差集，并将结果放入s
s.isdisjoint(t)   如果s和t没有相同项，则返回True
s.issubset(t)     如果s是t的一个子集，则返回True
s.issuperset(t)   如果s是t的一个超集，则返回True
```

## 文件：file
### 1. 使用open()函数操作文件时，一般需要经历如下步骤：
- 打开文件 f=open('xxx.txt','rb')
- 操作文件 f.readline()
- 关闭文件 f.close()
每次都要关闭文件很麻烦，with open('文件路径','模式') as filename: 这种方式来打开文件。

### 2. 打开文件的模式有：
- r ，只读模式【默认】
   - w，只写模式【不可读；不存在则创建；存在则清空内容；】
   - x， 只写模式【不可读；不存在则创建，存在则报错】
   - a， 追加模式【可读；   不存在则创建；存在则只追加内容；】
- "+" 表示可以同时读写某个文件
   - r+， 读写【可读，可写】
   - w+，写读【可读，可写】
   - x+ ，写读【可读，可写】
   - a+， 写读【可读，可写】
- "b"表示以字节的方式操作
   - rb  或 r+b
   - wb 或 w+b
   - xb 或 w+b
   - ab 或 a+b
注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，当以二进制的方式的效率比较高，因为磁盘底层是以字节存储

```
f.close()        关闭文件
f.fileno()       返回文件描述符
f.readline()     从当前指针读取一行
f.readlines()    从当前指针读取到结尾的全部行
f.read()         从当前指针读多少个字节,没有参数读取全部
f.tell()         告诉当前指针，是字节
f.seek(offset [whence])    移动指针，f.seek(0)把指针移动第一行第0个字节位置
    offset: 偏移量
    whence: 位置
        0: 从文件头
        1：从当前位置
        2：从文件尾部
f.write(string)    打开文件时，文件不存在，r,r+都会报错，其他模式则不会
f.writelines()     必须是字符串序列，把字符串序列当作一个列表写进文件
f.flush()          在文件没有关闭时，可以将内存中的数据刷写至磁盘
f.truncate()       文件截取多少字节保留,指针后面的内容全部会清空
f.name             是返回文件名字，不是方法，是属性    
f.closed           判断文件是否已经关闭
f.encoding         查看编码格式，没有使用任何编码，则为None
f.mode             打开文件的模式
f.newlines         显示出换行符的，空为默认\n不显示

文件迭代：
f = open('/etc/passwd','r')
for line in f:
    print(line)
```

### 3. 例子：

[读写文件的例子](https://github.com/xiaozhiqi2000/learn_python/blob/master/day02/file_do.py)

[修改ha.conf](https://github.com/xiaozhiqi2000/learn_python/blob/master/day02/change_ha_conf.py)

## 序列操作通用
```
s + r     连接
s * n     重复s的n次复制
v1,v2...vn = s     变量解包(unpack)
s[i]      索引
s[i:j]    切片
s[i:j:stride]      扩展切片
x in s,x not in s  成员关系
for x in s:        迭代
all(s)    如果s中的所有项都为True，则返回True
any(s)    如果s中的任意项为True，则返回True
len(s)    长度,元素个数
min(s)    s中的最小项
max(s)    s中的最大项
sum(s [,initial])    具有可选初始值的项的和
del s[i]     删除一个元素
del s[i:j]   删除一个切片
del s[i:j:stride]    删除一个扩展切片
```
### 1. 例子：

[市县级的三级联动](https://github.com/xiaozhiqi2000/learn_python/blob/master/day02/cityDict.py)

[购物车](https://github.com/xiaozhiqi2000/learn_python/blob/master/day02/shopCar.py)
