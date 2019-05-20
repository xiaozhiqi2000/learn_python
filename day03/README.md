# 今天主要内容
1. [函数](https://github.com/xiaozhiqi2000/learn_python/tree/master/day03#%E5%87%BD%E6%95%B0)
2. [lambda表达式](https://github.com/xiaozhiqi2000/learn_python/tree/master/day03#lambda-%E5%87%BD%E6%95%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F)
3. [内置函数](https://github.com/xiaozhiqi2000/learn_python/tree/master/day03#%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0)
4. [函数装饰器](https://github.com/xiaozhiqi2000/learn_python/tree/master/day03#%E5%87%BD%E6%95%B0%E8%A3%85%E9%A5%B0%E5%99%A8)

## 函数
1. 函数的定义

   函数是python为了代码最大程度地重用和最小化代码冗余而提供的基本结构
   ```
   def function_name(args):
       function_content
       return
   ```
2. 函数的返回值
   - 函数的返回值用return语句来返回结果，默认是返回None;
   - 返回多个值时，彼此间使用逗号分隔，且组合为元组形式返回一个对象;
   - 函数一旦执行到return,函数就终止了,如果return下面还有执行语句则终止
3. 函数的参数

   默认情况下，参数通过其位置进行传递，从左至右，这意味着，必须精确地传递和函数头部参数一样多的参数
   + 普通参数：定义函数时从左至右
     ```
     # name为普通参数也叫形式参数,简称：形参
     def f1(name):
         print(name)
     
     # 'tomcat' 叫做函数的实际参数,简称：实参
     f1('tomcat')
     ```
   + 默认参数：定义函数时是使用"name=value"的语法直接给变量一个值，从而传入的值可以少于参数个数
     ```
     # name 是普通参数,ab=5是默认参数
     def f1(name,ab=5):
         print(name,ab)
     
     # 使用默认参数
     f1('tomcat',12)
     
     注意：默认参数需要放在参数列表最后
     ```
   + 指定参数：调用函数时指定"name形式参数=value实际参数"的语法通过参数名进行匹配
      - 混用普通参数和默认参数，应当把默认参数写到右侧
      - 混用有默认和无默认值的参数时，无默认值放左侧
     ```
     # name 是普通参数,ab=5是默认参数
     def f1(name,ab=5):
         print(name,ab)
     
     # 指定参数
     f1(name='tomcat',ab=12)
     
     注意：默认参数需要放在参数列表最后
     ```
   + 动态参数：定义函数时形式参数中收集任意多基于普通参数
      - 定义函数时使用* ：收集普通参数，返回元组,*args
      - 定义函数时使用**：收集指定参数，返回字典,**kwargs
      - 调用函数时，使用\*或者\*\*开头的参数，从而传递任意多基于普通或指定参数
     ```
     # 俗称万能参数
     def f1(*args,**kwargs):
         print(args,type(args))
         print(kwargs,type(kwargs))
     
     # 执行方式一
     f1(11,22,33,k1='v1',k2='v2')
     
     # 执行方式二
     l1 = [1,2,3,4]
     d1 = {'a':'xiao','b':'zhi','c':'qi'}
     f1(*l1,**d1)
     ```
4. 函数的作用域
   - 全局变量全部用大写表示
   - 全局变量都可以被访问,函数内部的变量则为本地作用域
   - 在函数内如果要修改全局变量,需要global
   - 特殊:字典,列表可以在函数内修改,但是不能重新赋值
   - 满足LEGB：L是Local(本地变量),E是Excluding(嵌套变量),G是GOLAB(全局变量),B是Building(内建变量)
   - [更多作用域](http://www.cnblogs.com/xiaozhiqi/articles/5795637.html)

## lambda 函数表达式
- 对于简单的函数，也存在一种简便的表示方式，即：lambda表达式
- lambda表达式会自动return返回值,条件为真返回True,条件为假返回False.
  ```
  # ###################### 普通函数 ######################
  # 定义函数（普通方式）
  def func(arg):
      return arg + 1
      
  # 执行函数
  result = func(123)
      
  # ###################### lambda ########################
      
  # 定义函数（lambda表达式）
  my_lambda = lambda arg1, arg2=50 : arg1 + arg2 + 1
      
  # 执行函数
  result = my_lambda(123, 23)
  ```

## 内置函数
[官网详解](https://docs.python.org/3/library/functions.html#next)

![avatar](/day03/imgs/inter_function.png)

[内置函数查看](https://github.com/xiaozhiqi2000/learn_python/blob/master/day03/build_function.md)

## 函数装饰器

　装饰器可以使函数执行前和执行后分别执行其他的附加功能，这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)，装饰器的功能非常强大。装饰器一般接受一个函数对象作为参数，以对其进行增强

- 装饰器本身是一个函数，用于装饰其他函数
- 功能：增强被装饰函数的功能
- 装饰器是一个闭包函数是嵌套函数，通过外层函数提供嵌套函数的环境
- 装饰器在权限控制，增加额外功能如日志,发送邮件用的比较多

1. 单层装饰器

```
def outer(func):
    def inner(*args,**kwargs):
        print("before")
        ret = func(*args,**kwargs)
        print("after")
        return ret
    return inner

@outer
def f1(*args, **kwargs):
    print("F1")
    return "是你"

ret = f1("aaaaaaaa")
print("返回值是:",ret)

解释:
(1)碰到def outer(func)就把函数体加载到内存

(2)碰到@outer装饰器就会自动执行outer()函数并把f1这个函数名通过参数传递到outer(f1),f1重新赋值为inter这个函数体

(3)碰到def inner()就把函数体加载内存
   - 1.此时inner()函数体中就有了print("before"),print("F1"),print("after")3句代码
   - 2.并将返回值赋值给变量ret,然后return rest返回
   - 3.python碰到return同一级代码不再执行了,此时inner()函数就结束了(因为inner函数没有调用,所以没有执行)

(4)碰到ret = f1(),f1()被调用了就会执行f1函数就会执行inner的函数体,并用ret接收返回值

(5)就print(ret)打印出返回值
```

2. 双层装饰器

  当一个装饰器不够用的话，我们就可以用两个装饰器，当然理解起来也就更复杂了，当使用两个装饰器的话，首先将函数与内层装饰器结合然后在与外层装饰器相结合，要理解使用@语法的时候到底执行了什么，是理解装饰器的关键。这里还是用最简单的例子来进行说明。

```
def outer2(func2):
    def inner2(*args,**kwargs):
        print('开始')
        r=func2(*args,**kwargs)
        print('结束')
        return r
    return inner2
 
def outer1(func1):
    def inner1(*args,**kwargs):
        print('start')
        r=func1(*args,**kwargs)
        print('end')
        return r
    return inner1
 
@outer2                                # 这里相当于执行了 f=outer1(f)  f=outer2(f)，步骤如下
@outer1                                # 1、f=outer1(f) f被重新赋值为outer1(1)的返回值inner1，
def f():                               #    此时func1为 f():print('f 函数')
    print('f 函数')                    # 2、f=outer2(f) 类似f=outer2(inner1) f被重新赋值为outer2的返回值inner2
                                       #    此时func2 为inner1函数 inner1里面func1函数为原来的 f():print('f 函数')
                                                                          
f()                                    # 相当于执行 outer2(inner1)()

执行结果如下：
开始                                   # 在outer函数里面执行，首先打印 ‘开始 ’
start                                  # 执行func2 即执行inner1函数 打印 ‘start’
f 函数                                 # 在inner1函数里面执行 func1 即f()函数，打印 ‘f 函数’
end                                    # f函数执行完，接着执行inner1函数里面的 print('end')
结束                                   # 最后执行inner2函数里面的 print('结束')

```











