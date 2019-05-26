# 今天主要内容
1. [面向对象]()
2. [三大特性之封装]()
3. [三大特性之继承]()
4. [三大特性之多态]()

## 面向对象

面向对象是一种编程方式，使用 “类” 和 “对象” 来实现，所以，面向对象编程其实就是对 “类” 和 “对象” 的使用。类就是一个模板，模板里可以包含多个方法（函数），方法里实现各种各样的功能，对象则是根据模板创建的实例，通过实例，对象可以执行类中的方法，每个对象都拥有相同的方法，但各自的数据可能不同。
```
class F1():  
    def __init__(self,name,age):  
        self.name = name 
        self.age = age
     
f1 = F1('python',27)   
     
上面的这个__init__()叫做构造方法，可有可无，如需要在对象创建的会执行这个方法，如需要在创建对象的时候给对象添加些属性，执行方法就可以在构造函数里面操作。如果没有写这个函数，那么创建对象的时候不会有什么操作的。

参数self有什么用呢？ 

1.在内存中开辟一块空间指向f1这个变量名，self永远是执行该方法的调用者
2.实例化F1这个类首先执行其中的__init__()方法，相当于F1.__init__(f1,'python',27),是为了把'python',27这2个值跟刚开辟的f1关联起来，因为关联起来后，你就可以直接f1.name, f1.age 这样来调用啦。所以，为实现这种关联，在调用__init__方法时，就必须把f1这个变量也传进去，否则__init__不知道要把那2个参数跟谁关联，self其实就是实例化对象f1被当作参数传递了。
3.所以这个__init__(…)构造方法里的，self.name = name , self.age = age 等等就是要把这几个值存到f1的内存空间里。
```
## 封装
#### 1. 第一种封装(但是我们不会这么用)
```
class A():
  
    def f1(self):
        print(self.name)  
        print(self.age)    
  
a=A()                      # 创建对象a 
a.name="hello"             # 将a.name="hello" 封装进a对象里面了
a.age=18                   # 将a.name=18 封装了a对象里面了
a.f1()                     # 因为self就是a这个对象,所以执行a.f1()可以打印"hello"和18
```
#### 2. 第二种封装(通过构造方法,常用)
```
class A():
    def __init__(self,name,age)  
        self.name = name
        self.age = age
 
    def f1(self):
        print(self.name) 
        print(self.age) 
 
a=A("hello",18)            # 创建对象a,self=a,那么在构造方法里面就相当于a.name="hello",a.age=18
a.f1()                     # 因为self就是a这个对象,所以执行a.f1()可以打印"hello"和18
```
#### 3. 第三种封装(复杂封装将类封装进对象中)
```
class c1():
 
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj
 
class c2():
 
    def __init__(self,name,age):
        self.name = name
        self.age = age
 
    def show(self):
        print(self.name)
 
class c3():
 
    def __init__(self,a1):
        self.money = 123
        self.aaa = a1
 
c2_obj = c2('aa',12)          # 将字符串'aa',数字12封装到c2_obj.name和c2_obj.age中
c1_obj = c1('python',c2_obj)  # 将字符串'python'封装到c1_obj.name中，将c2_obj中的属性c2_obj.name,c2_obj.age封装到c1_obj.obj中
c3_obj = c3(c1_obj)           # 将c1_obj中的所有属性,包括(c2_obj的所所有方法和属性)
 
print(c3_obj.aaa.obj.name)    # c3类中找到c2类中的属性,1. c3_obj.aaa=c1_obj 2. c1_obj.obj=c2_obj 3. c2_obj.name="aa"
ret = c3_obj.aaa.obj.show()   # c3类中找到c2类中的方法执行并接收返回值
print(ret)
```
#### 4. 例子
[游戏人生](https://github.com/xiaozhiqi2000/learn_python/blob/master/day11/gameClass.py)

## 继承

继承的本质是将父类中的方法全部复制一份到子类中。Python里面的继承可以多继承，通过继承，可以获得父类的功能，继承的时候，如果父类中有重复的方法，优先找自己。通过继承创建的新类称为“子类”或“派生类”。被继承的类称为“基类”、“父类”或“超类”。
```
class A():
    def f(self):
        print('a')

class B(A):
    def f1(self):
        print('b')

这里B这个类就继承了A的所有
```
#### 1. 继承之重写(不想继承父类某个方法)
```
class A():
    def __init__(self):
        print("A.init")

    def f(self):
        print("A")
  
class B(A):

    def f(self):
       print("B")
  
obj=B()  # B继承了A，那么B就有了A全部方法属性，包括构造方法，所以这里创建obj对象后会打印'a'
obj.f()  # B类有f()方法，A类也有f()方法，所以不会执行A类中的f1()方法
```
#### 2. 继承之使用父类方法
```
class A():
    def __init__(self):
        print("A.init")

    def f(self):
        print("A")
 
class B(A):

    def f(self):
       super(B,self).f() # 第一种super(当前类,self).父类方法
       A.f(self)         # 第二种父类.父类方法(self)将self传进去
       print("B")
 
obj=B()  # B继承了A，那么B就有了A全部方法属性，包括构造方法，所以这里创建obj对象后会打印'a'
obj.f()  # B类有f()方法，A类也有f()方法，因为使用了父类方法，所以会执行A类中的f1()方法和本身的print("B")
```
#### 3. 继承之代码执行流程
- 继承多个父类，从第一个父类开始寻找，然后第二个父类找
- 左边一直找到最上面那个父类，如果没有找到，就从第二个类开始寻找
- 如果两个父类中又有共同的父类，在第一个有共同父类的那个类就不会往共同父类找了，会往第二个父类开始找，最后找共同的父类
- self 永远是执行该方法的调用者
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BaseRequest():

    def __init__(self):
        print('BaseRequest.init')


class RequestHandler(BaseRequest):

    def __init__(self):
        print('RequestHandler.init')
        BaseRequest.__init__(self)

    def server_forever(self):
        print('RequestHandler.server_forever')
        self.process_request()

    def process_request(self):
        print('RequestHander.process_request')


class Minx:

    def process_request(self):
        print('minx.process_request')


class Son(Minx, RequestHandler):

    pass

obj = Son()
obj.process_request()

代码执行过程是这样的：
1. obj=Son()那么会执行Son()类中的构造方法，Son()没有就往第一个父类Minx()找他的__init__()方法，没有就继续往下找
2. ojb.server_forever() 先到Son()类中找，没有就往第一个父类Minx()找，没有就往RequestHander()类中找，找到了
3. server_forever() 执行了print('RequestHandler.server_forever')和self.process_request()
4. self.process_request() 执行了self.process_request()，那么要回到obj = Son()重新开始找，self 永远是执行该方法的调用者
5. 结果在Minx()第一个父类中找到了process_request(self)，所以不会执行RequestHandler()中的process_request(self)方法
```

## 多态

Python不支持Java和C#这一类强类型语言中多态的写法，python本身就是支持多态的，所以在Python面向对象里面讨论多态并没有什么意义，其Python崇尚“鸭子类型”。
```
def f(arg):
    print(arg)

obj = f("hello")
obj = f(12)
obj = f(["hello",12])

arg这个形态就可以多种形态,可以是字符串,可以数字,可以列表,可以字典,都可以
但是在其他语言中却不能这样定义,必须要定义是什么形态的比如def f(string arg),那么arg只能是字符串这种形态
如果ojb = f(11)就会报错，只能传入字符串,obj=f("hello")才不会报错
```
