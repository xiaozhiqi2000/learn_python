##### help() 详细查看某个类有那些方法或者方法的具体使用
```
help(str)
help(str.strip)
```

##### dir() 快速查看某个类有那些方法或者方法的具体使用
```
dir(str)
dir(str.strip)
```

##### int() 实例化数字类型,或将其他类型转换为数字类型,或各种进制转换为十进制
```
(1)实例化数字类型
i = int(23)
print(type(i),i)
<class 'int'> 23

(2)将数字字符串转换为数字类型,只能时数字字符串才能转为数字类型,否则报错
s = "123"
type(s)
<class 'str'>

i = int(s)
print(type(i),i)
<class 'int'> 123

(3)将二进制转换为十进制
print(int('11',base=2))
3
```

##### float() 实例化浮点类型,或将数字字符串转换为浮点型,仅限于数字字符串
```
(1) 实例化浮点类型
f = float(12)
print(type(f),f)
<class 'float'> 12.0

(2) 将数字字符串转换为浮点类型
s = "12"
type(s)
<class 'str'>

i = float(s)
print(type(i),i)
<class 'float'> 12.0
```

##### str() 实例化字符串类型,或将其他类型转换为字符串类型
```
(1) 实例化字符串类型
s = "python"
print(type(s))
<class 'str'>

(2) 将其他类型转换为字符串类型了
s = 88888
type(s)
<class 'int'>

i = str(s)
print(type(i),i)
<class 'str'> 88888

l = [1,2,3,4,5]
a = str(l)
print(type(a),a)
<class 'str'> [1, 2, 3, 4, 5]
注意：列表格式或字典格式的字符串类型转换为列表或者字典需要使用json模块
```

##### list() 将其他类型转为列表类型
```
(1) 实例化列表类型
l = list(["redhat","centos","ubuntu"])
print(type(l),l)
<class 'list'> ['redhat', 'centos', 'ubuntu']

(2) 将其他类型转换为列表
s = "python"
l = list(s)
print(type(l),l)
<class 'list'> ['p', 'y', 't', 'h', 'o', 'n']

t = ("python","I","like")
l1 = list(t)
print(type(l1),l1)
<class 'list'> ['python', 'I', 'like']
```

##### tuple() 实例化元组类型,或将其他类型转换为元组类型
```
(1) 实例化元组类型
t1 = tuple(("redhat","centos","ubuntu","opensuse"))
print(type(t1),t1)
<class 'tuple'> ('redhat', 'centos', 'ubuntu', 'opensuse')

(2) 将其他类型转换为元组类型
l = [11,22,33,44,55]
type(l)
<class 'list'>

t = tuple(l)
print(type(t),t)
<class 'tuple'> (11, 22, 33, 44, 55)
```

##### dict() 实例化字典,或将元组列表转换为字典类型仅限元组形式列表类型
```
(1) 实例化字典类型
d1 = dict({"os":"ubuntu","version":15.10,"kernel":"4.2.0-16"})
print((d1),d1)
<class 'dict'> {'version': 15.1, 'os': 'ubuntu', 'kernel': '4.2.0-16'}

(2) 将元组形式的列表转换为字典
l3 = [('a',1),('b',11),('c',45)]
d2 = dict(l3)
print(type(d2),d2)
<class 'dict'> {'b': 11, 'c': 45, 'a': 1}

注意：zip()这个内置方法可以将两个列表生成元组形式列表类型
```


##### set() 实例化可变集合类型,或其他类型转换成集合类型
```
(1) 实例化集合类型
s = set({"fedora","geentoo","debian","centos"})
print(type(s),s)
<class 'set'> {'fedora', 'centos', 'debian', 'geentoo'}

(2) 将其他类型转换成集合set类型
l = ["centos","centos","redhat","ubuntu","suse","ubuntu"]
s = set(l)
print(type(s),s)
<class 'set'> {'ubuntu', 'centos', 'redhat', 'suse'}

d = {"kernel":"Linux","os":"ubuntu","version":"15.10"}
s = set(d.keys())
print(type(s),s)
<class 'set'> {'kernel', 'version', 'os'}
```

##### frozenset() 实例化不可变集合,或类型转换成不可变集合类型
```
(1) 实例化不可变集合
fs = frozenset({"redhat","centos","fedora","debian","ubuntu"})
print(type(fs),fs)
<class 'frozenset'> frozenset({'fedora', 'ubuntu', 'centos', 'debian', 'redhat'})

(2) 类型转换成不可变集合
l = [1,2,3,4,4,5,5]
fs1 = frozenset(l)
print(type(fs1),fs1)
<class 'frozenset'> frozenset({1, 2, 3, 4, 5})
```

##### bool() 0,"",None,[],(),{}都为假,其余都为真,是int的子类
```
bool(0)
False

bool("abc")
True

bool("")
False

bool([])
False

bool()
False

issubclass(bool, int)
True
```

##### bytes() 将字符串类型转换成字节byte类型,在计算机底层都是以二进制存储数据的
```
1bytes = 8bit,一个汉字utf8是用3个字节存储,一个汉字gbk是用2个字节存储,一个字母数字是1字节
bytes(要转换的字符串,按照什么编码)

(1) 将字符串转换为字节类型
>>> s = "大神"
>>> p = bytes(s,encoding="utf-8")
>>> print(type(p),p)
<class 'bytes'> b'\xe8\x9f\x92\xe8\x9b\x87'

(2) 将字节类型重新转换为字符串
>>> new_s = str(p,encoding="utf-8")
>>> print(type(new_s),new_s)
<class 'str'> 大神

注意: 在文件对象处理的时候注意打开的模式如果以wb模式打开,则写入的数据需要转换成bytes()写入
```

##### bytearray() 和bytes()是一样的,只是返回一个byte列表

```
bytearray类型是一个可变的序列，并且序列中的元素的取值范围为 [0,255]

a = bytearray("大神",encoding="utf-8")
print(type(a),a)
<class 'bytearray'> bytearray(b'\xe8\x9f\x92\xe8\x9b\x87')

a[0]
232
a[1]
159
a[2]
146
a[4]
155
a[5]
135
```

##### open() 是打开一个文件对象,用于对文件的操作处理
```
with open("/etc/passwd","r") as f:
    for line in f:
        print(line)

注意: 具体的操作,请查看文件对象这边博客
```

##### type() 查看某个实例属于哪个类型
```
s = "python"
l = [1,2,3,4]
t = ("linux","python")
d = {"name":"linux","age":12}
print(type(s),type(l),type(t),type(d))
<class 'str'> <class 'list'> <class 'tuple'> <class 'dict'>
```

##### id() 查看对象在内存中的地址
```
s = "python"
id(s)
139639742647240

l = [1,2,3,4]
id(l)
139639704025736
```

##### len() 查看实例中的长度,说白点就是元素个数
```
python2.x是以字节计算,python3.x是以字符计算

s = "python"
len(s)
6

s = "大神"
len(s)
2

python3.x如果需要以字节计算,要先转换成bytes()
b = bytes(s,encoding="utf-8")
len(b)
6
```

##### input() 输入,默认输入的格式为字符串,输入的数字也是字符串,需要int()转换,python2.x是用ray_input()方法
```
data = input("please say something:")
please say something:today is good day
print(data)
today is good day

data1 = input("please say something:")
please say something:123
print(type(data1),data1)
<class 'str'> 123

print() 输出,格式化输出
name = "python"
print("I love %s" % name)
I love python

注意: 具体查看格式化输出相关博客
```

##### all() 接收一个迭代对象
```
0,"",None,[],(),{}都为假,all是全部为真则为真,有一个假则为假

s = ["python","php","java"]
print(all(s))
True

a = ["","python","php"]
print(all(a))
False
```

##### any() 只要有一个为真则为真,全为假则为假
```
a = ["","python","php"]
print(any(a))
True

s = ["",0,(),[],{},None]
print(any(s))
```

##### max(),min(),sum() 一般是数字系列中的最大,最小,求和
```
r = max([11,22,33])
print(r)
33

r1 = min([11,22,33])
print(r1)
11

r2 = sum([11,22,33])
print(r2)
65
```

##### abs() 求绝对值
```
print(abs(-123))
123
```

##### pow() 求几次方和**是一样的
```
print(pow(2,10))
1024

2**10
1024
```

##### round() 四舍五入
```
print(round(18.8))
19

print(round(18.4))
18
```

##### divmod() 除法得余数,在分页功能中会用到
```
print(divmod(78,10))
(7, 8)

print(divmod(45,10))
(4, 5)
```

##### chr() ascii表的对应关系,十进制数字转为字符
##### ord() ascii表的对应关系,将ascii字符转为数字
```
>>> r = chr(65)
>>> print(r)

>>> n = ord("a")
>>> print(n)

注意:利用这两个函数和random可以实现随机数字字母验证码,最后有代码
```

##### bin() 十进制转二进制
##### oct() 十进制转八进制
##### hex() 十进制转十六进制
```
print(bin(5))
print(oct(9))
print(hex(15))
```

##### enumerate() 枚举类型,实现循环的时候打印出行号,默认是0开始,也可以设置1开始
```
li = ["redhat","centos",'fedodra']
for index,data in enumerate(li):
    print(index,data)

0 redhat
1 centos
2 fedodra

li = ["redhat","centos",'fedodra']
for index,data in enumerate(li,1):
    print(index,data)

1 redhat
2 centos
3 fedodra
```

##### sorted() 排序,不能数字和字母在一起排序和list.sorted()是一样的,python2.x是可以混合排序的
```
l1 = [1,5,2,55,33]
a = sorted(l1)
print(a)
[1, 2, 5, 33, 55]

l2 = [1,5,2,55,33,66]
l2.sort()
print(l2)
[1, 2, 5, 33, 55, 66]
```

##### reversed() 逆序和list.reverse()是一样的
```
>>> l3 = [33,22,55,11]
>>> a = reversed(l3)
>>> print(list(a))

>>> l4 = [33,22,55,11,44]
>>> l4.reverse()
>>> print(l4)
[44, 11, 55, 22, 33]
```

##### slice() 和字符串列表的切片的功能是一样的
```
s = "python"
s[0:4]
'pyth'
s[0:4:2]
'pt'

b = slice(0,4,2)
print(b)
slice(0, 4, 2)
s[b]
'pt'
```

##### zip() 取一个或多个序列为参数,把序列中的并排元素配成元组,返回元组形式的列表类型,当元素长度不同时以最短序列的长度为准
```
l1 = ['烧饼',11,22,33]
l2 = ['is',11,22,33]
l3 = ['sb',11,22,33]
r = zip(l1,l2,l3)
print(list(r))
[('烧饼', 'is', 'sb'), (11, 11, 11), (22, 22, 22), (33, 33, 33)]

temp = list(r)[0]
ret = ' '.join(temp)
print(ret)
烧饼 is sb

两个列表合成一个字典:
keys = [1,2,3,4,5,6,7]
vaules = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
D = {}
for (k,v) in zip(keys,values):
    D[k] = v

print(D)
{1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
```

##### compile() 将代码编译成python代码
##### eval() 只能执行表达式,并且返回结果
##### exec() 执行python代码或者先编译成python代码再执行,接收：代码或者字符串,没有返回结果
```
s = "print(123)"
r = compile(s,"<string>","exec")
exec(r)
123

exec和eval的区别:
exec("7+8+9")
ret = eval("7+8+9")
print(ret)
24
```

##### complex() 创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
```
参数real: int, long, float或字符串；
参数imag: int, long, float。

complex(1, 2)
(1 + 2j)

complex(1) #####数字
(1 + 0j)

complex("1") #####当做字符串处理
(1 + 0j)

complex("1+2j")
(1 + 2j)

注意：这个地方在“+”号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
```

##### globals() 显示所有的全局变量
##### locals() 显示所有的局部变量
```
NAME = 'tomcat'
def show():
    a = 123
    b = 456
    print(locals())
    print(globals())
show()
```

##### vars() 本函数是实现返回对象object的属性和属性值的字典对象。如果默认不输入参数，就打印当前调用位置的属性和属性值，相当于locals()的功能。如果有参数输入，就只打印这个参数相应的属性和属性值。
```
class Foo: 
    a = 1 
    print(vars(Foo)) 

foo = Foo() 
print(vars(foo))
```

##### callable() 判断是否可以被调用
```
def f1():
    pass

print(callable(f1))

f2 = 123
print(callable(f2))
```

##### range() 在python2中有xrange和range，其中range会一次在内存中开辟出了所需的所有资源，而xrange则是在for循环中循环一次则开辟一次所需的内存，而在Python3中没有xrange，只有range ，但是python3的range代表的就是xrange。range用来指定范围，生成指定的数字。
```
for i in range(4): 
    print(i)

0
1
2
3

for i in range(1,4,2): 
    print(i)

1
3
```

##### format() 格式化输出的,和百分号是同样的功能
```
>>> print("1 am {},age {}".format('jason',18)) ##### 用{}当作占位符
>>> print("1 am {},age {}".format(*['jason',18])) ##### 用*传递一个列表进去
>>> print("1 am {0},age {1}，score{1}".format('jason',18)) ##### 1 am jason,age 18，score18 用 0，1等数字来应用

注意: 具体查看格式化输出相关
```

##### hash() 一般用在字典中的Key是进行hash计算后,值存入内存,hash值
```
>>> dic = {'name':'SB'}
>>> print(hash(dic['name']))
```

##### filter() filter(函数,可迭代对象),fileter内部,循环第二个参数,将每一个元素执行第一个函数
```
如果函数返回值True,表示元素合法,就把元素存入结果ret中

def f2(a):
    if a>22:
    return True

li = [11,22,33,44,55]
ret = filter(f2,li)
print(list(ret))

注意: 对于简单的函数用lambda可以实现
result = filter(lambda a: a > 33,li)
print(list(result))
```

##### map() map(函数,可迭代的对象),循环第二个参数,将每一个元素执行第一个函数,就把返回值存入结果result中
```
l1 = [11,22,33,44,55,66]
def f3(a):
    return a + 100

result = map(f3,l1)
print(list(result))

注意: 对于简单的函数用lambda可以实现
result = map(lambda a: a + 100,l1)
print(list(result))
```

##### iter() 用于生成迭代器,for循环就是调用iter()生成迭代对象
##### next() 用于遍历迭代器,for循环就是调用next()实现,不过当使用next()遍历时,迭代器没有元素时会报错,for则不会
```
a = iter([1,2,3,4,5])
a
<list_iterator object at 0x101402630>
a.__next__()
1
a.__next__()
2
a.__next__()
3
a.__next__()
4
a.__next__()
5
a.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

##### hasattr() 判断模块中是否有某个函数名
##### getattr() 获取模块中的函数名
##### setattr() 设置模块中的函数名
##### delattr() 删除模块中的函数名
##### __import__() 以字符串的形式导入模块,相当于import 模块名
```
根据URL的不同调用不同的函数处理

def run():
    inp = input("请输入要访问的URL:")
    mo,fn = inp.split('/')
    obj = __import__(mo)   ##### 以字符串的形式导入mo模块并设置一个别名obj,相当于import mo as obj
    if hasattr(obj,fn):    ##### 判断mo模块中是否有fn函数名(函数名指向函数体)
        func = getattr(obj,fn)   ##### 有的话设置一个变量赋值给这个函数体
        func()                   ##### 执行函数
    else:
        print("网页不存在")

run()
```

##### isinstance() 检查对象是不是某个类的对象,或者某个父类的对象
##### issubclass() 检查类是否是某个类的子类
```
class Bar:

    def __iter__(self):
        yield 1
        yield 2

class Foo(Bar):
    pass

obj = Foo()

ret1 = isinstance(obj,Foo)
print(ret1)

ret2 = isinstance(obj,Bar) ##### obj,Bar(obj类型和obj类型的父类) 的实例
print(ret2)

ret3 = issubclass(Foo,Bar)
print(ret3)
```

##### super() 继承中强制使用父类中的方法
```
class C1:

    def f1(self):
        print('c1.f1')
        return 123

class C2(C1):

    def f1(self):
        ##### 主动执行父类的f1方法
        ret = super(C2,self).f1()
        print('c2.f1')
        return ret

obj = C2()
obj.f1()
```

##### property() 将函数当作属性访问
```
class Pager:

    def __init__(self,all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self,value):
        print(value)

    def  f3(self):
        print("del p.foo")

    foo = property(fget=f1,fset=f2,fdel=f3)


p = Pager(101)
result = p.foo
print(result)

p.foo = "python"

del p.foo
```

##### staticmethod()  类中定义类方法,可以任意参数
##### classmethod()   类中定义类方法,至少有一个参数cls,cls指类名,python自动传递
```
class Province:
    country = "中国"

    def __init__(self,name):
        self.name = name

    ##### 普通方法，由对象调用执行（方法属于类）,实例化才能调用
    def show(self):
        print(self.name)

    @staticmethod
    def f1(arg1,arg2):  ##### 可以没有参数，或者任意参数
        ##### 静态方法，由类调用执行
        print(arg1,arg2)

    @classmethod
    def f2(cls): ##### 至少要有cls一个参数,cls就是类名，python自动会传，就像self
        print(cls)

Province.f1(1111,2222)
Province.f2()
