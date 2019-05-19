# 今天主要内容
1. 函数
2. 内置函数
3. lambda表达式
4. 函数装饰器

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
1. 装饰器和知识储备
2. 原函数不带参数的装饰器
3. 原函数带参数的装饰器
4. 使用两个装饰器
5. 带参数的装饰器
