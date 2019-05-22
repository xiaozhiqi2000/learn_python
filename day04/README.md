# 今天主要内容
1. [生成器]()
2. [列表解析]()
3. [迭代器]()
4. [迭代器表达式]()
5. [递归]()
6. [深浅复制]()

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

迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件

特点：
1. 访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
2. 不能随机访问集合中的某个值，只能从头到尾依次访问
3. 访问到一半时不能往回退
4. 便于循环比较大的数据集合，节省内存
5. next()就相当于调用__next__()，for也是
6. iterable(可迭代)对象
7. 支持每次返回自己所包含的一个成员的对象
8. 对象实现了__iter__方法,实际使用 for 循环取值即可
   - 序列类型，如 str,list,tuple,set
   - 非序列类型，如 dict, file
   - 用户自定义的一些包含了__iter__()或__getitem__()方法的类

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

![avatar](/day04/imgs/digui.png)

传入1的时候，n=2不满足n>=4这个条件，return func(2)

传入2的时候，n=3不满足n>=4这个条件，return func(3)

传入3的时候，n=4满足n>=4这个条件，return end

return end --> return func(3) --> return func(2) --> r = func(1) 所以r的返回值就是end

