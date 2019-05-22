# 今天主要内容
1. [生成器](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E7%94%9F%E6%88%90%E5%99%A8)
4. [生成器器表达式](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E7%94%9F%E6%88%90%E5%99%A8%E8%A1%A8%E8%BE%BE%E5%BC%8F)
3. [迭代器](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E8%BF%AD%E4%BB%A3%E5%99%A8)
2. [列表解析](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E5%88%97%E8%A1%A8%E8%A7%A3%E6%9E%90)
5. [递归](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E9%80%92%E5%BD%92)
6. [深浅复制](https://github.com/xiaozhiqi2000/learn_python/tree/master/day04#%E6%B7%B1%E6%B5%85%E5%A4%8D%E5%88%B6)

## 生成器

一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator）；如果函数中包含yield语法，那这个函数就会变成生成器；能够用next()调用或for循环使用

```
def func():
    print("start")
    yield 1
    yield 2

temp = func()

temp.__next__()
start
1
temp.__next__()
2
temp.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

func是函数称为生成器，当执行此函数func()时会返回一个迭代器给temp
通过__next__方法取值，第一次执行print("start") 将yield 1的1返回给temp并打印temp
第二次执行到了yield 2将2返回给temp并打印temp，没有值可取就会报错
所以一般不用__next__()方法，直接使用 for 循环直接取值就好了，而且不会报错

for i in temp:
    print(i)

start
1
2
```
### 例子：

[yield例子](https://github.com/xiaozhiqi2000/learn_python/blob/master/day04/yieldExample.py)

[使用yield自定义range函数](https://github.com/xiaozhiqi2000/learn_python/blob/master/day03/definrYieldExample.py)

## 生成器表达式

生成器表达式并不真正创建数字列表，而是返回一个生成器对象，此对象在每次计算出一个条目后，把这个条目“产生”(yield)出来 
生成器表达式使用了"惰性计算"或称作"延迟求值"的机制
序列过长，并且每次只需要获取一个元素时，应当考虑使用生成器表达式而不是列表解析
生成器表达式与python 2.4引入
```
(expr for iter_var in iterable)
(expr for iter_var in iterable if condition_expr)

示例1：    
g1 = ( i**2 for i in range(1,11))
next(g1)
1
next(g1)
4
    
示例2：    
for j in ( i**2 for i in range(1,11) ):
    print(j/2)
```

## 迭代器

迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件，仅需通过next()方法不断去取下一个内容，便于循环比较大的数据集合，节省内存，next()就相当于调用__next__()，直接使用for取值即可，for也是调用__next__

```
a = iter([1,2,3])
a.__next__()
1
a.__next__()
2
a.__next__()
3
a.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  StopIteration

或者调用next()方法
l1 = [1,2,3]
l2 = l1.__iter__()
next(l2)
1
next(l2)
2
next(l2)
3
next(l2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  StopIteration

```

## 列表解析
列表解析是python迭代机制的一种应用，它常用于实现创建新的列表，因此要放置于[]中
```
[expression for iter_var in iterable]   
[expression for iter_var in iterable if condition_expression]

l1 = [1,2,3,4,5]

l2 = [x ** 2 for x in l1]

print(l2)
[1, 4, 9, 16, 25]
```
### 例子：

[列表解析例子](https://github.com/xiaozhiqi2000/learn_python/blob/master/day04/iterableExample.py)

## 递归

如果一个函数在其内部调用它自己，就叫做递归，但是递归的时候要设置一个退出递归的条件，不然会一直递归下去，变成一个死循环。从另一个方面来说，递归其实和循环其实是等价的。想要明白递归的话，我们先从实际的例子上来说明这一点，比如说我们要写一个阶乘函数 f(n)算出n的阶乘，阶乘函数实现的方法很多，下面讲如何用递归实现

```
示例1：
def f(n):
    if 0==n:                　　# n=0 的话直接返回空，对用户输入的零进行判断
        return None
    elif 1==n:              　　# n=1 的话就不再递归
        return n
    else:
        return n*f(n-1)    　　 # 递归在执行f(n-1) 直到f（1）

print(f(5))                　　 # 120

f(5)的执行过程如下:
    ===> f(5)
    ===> 5 * f(4)
    ===> 5 * (4 * f(3))
    ===> 5 * (4 * (3 * f(2)))
    ===> 5 * (4 * (3 * (2 * f(1))))
    ===> 5 * (4 * (3 * (2 * 1)))
    ===> 5 * (4 * (3 * 2))
    ===> 5 * (4 * 6)
    ===> 5 * 24
    ===> 120

示例2：
def func(n):
    n += 1
    if n >= 4:
        return 'end'
    return func(n)

r = func(4)
print(r)

end  #这是执行结果
```

下面的图帮助理解:

![avatar](/day04/imgs/digui.jpg)

传入1的时候，n=2不满足n>=4这个条件，return func(2)

传入2的时候，n=3不满足n>=4这个条件，return func(3)

传入3的时候，n=4满足n>=4这个条件，return end

return end --> return func(3) --> return func(2) --> r = func(1) 所以r的返回值就是end

## 深浅复制

拷贝意味着对数据重新复制一份，对于拷贝有两种深拷贝，浅拷贝两种拷贝，不同的拷贝有不同的效果。拷贝操作对于基本数据结构需要分两类进行考虑，一类是字符串和数字，另一类是列表、字典等。如果要进行拷贝的操作话，要import copy

### 1.数字和字符串

对于数字和字符串而言，深拷贝，浅拷贝没有什么区别，因为对于数字数字和字符串一旦创建便不能被修改，假如对于字符串进行替代操作，只会在内存中重新生产一个字符串，而对于原字符串，并没有改变，基于这点，深拷贝和浅拷贝对于数字和字符串没有什么区别，下面从代码里面说明这一点
```
import copy
s='abc'
print(s.replace('c','222'))         # 打印出 ab222
print(s)                            # s='abc' s并没有被修改
s1=copy.deepcopy(s)
s2=copy.copy(s)
 
#可以看出下面的值和地址都一样，所以对于字符串和数字，深浅拷贝不一样，数字和字符串一样就不演示了，大家可以去试一下
print(s,id(s2))                     # abc 1995006649768
print(s1,id(s2))                    # abc 1995006649768
print(s2,id(s2))                    # abc 1995006649768
```
### 2.列表和字典
对于字典、列表等数据结构，深拷贝和浅拷贝有区别，从字面上来说，可以看出深拷贝可以完全拷贝，浅拷贝则没有完全拷贝，下面先从内存地址分别来说明，假设 n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}。

```
下面从代码上来进行说明，copy.copy()与list.copy(),dict.copy()都属于浅复制
import copy
n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
n2=copy.copy(n1)　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 # 浅拷贝
n3=copy.deepcopy(n1)　　　　　　　　　　　　　　　　　　　　　　　　　　　　# 深拷贝
print(n1,id(n1),id(n1['k1']),id(n1['k3']))
print(n2,id(n2),id(n2['k1']),id(n2['k3']))
print(n3,id(n3),id(n3['k1']),id(n3['k3']))
 
从下面打印的值结合上面的图就可以很好的理解
{'k3': ['alex', 456], 'k2': 123, 'k1': 'wu'} 2713748822024 2713753080528 2713755115656　　　　　　
{'k3': ['alex', 456], 'k2': 123, 'k1': 'wu'} 2713755121416 2713753080528 2713755115656
{'k3': ['alex', 456], 'k2': 123, 'k1': 'wu'} 2713753267656 2713753080528 2713754905800
```

