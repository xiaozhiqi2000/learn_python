#今天主要内容
1. 数据类型
- 数字：int float
- 字符：str
- 列表：list
- 元组：tuple
- 集合：set frozenset
- 文件：file
![avatar](/day03/imgs/inter_function.png)

##数字：int float

python的数字字面量：整数，布尔型，浮点数，复数，所有数字类型均为不可变
- int（整型）
   - 在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647
   - 在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807
- bool(布尔型)
   - 真或假
   - 1 或 0
- float(浮点型)
- 数字操作：+ , -, *, /, //, **, %, -x, +x

##字符：str 不可变对象

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

##列表：list 可变对象
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

##元组：tuple 不可变对象
```
tuple.count() 统计元组中元素的个数
tuple.index() 找出元组中元素的索引位置
```

##字典：dict
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
```

##集合：set 
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

##文件：file
