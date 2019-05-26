# 今天主要内容
1. [类成员]()
1. [类成员之属性]()
2. [类成员之方法]()
3. [类成员之包装]()
4. [类的特殊成员]()


## 类成员
类的成员可以分为三大类：属性、方法和包装

(很重要的一句话，实例可以访问实例属性和方法包括类中的所有属性和方法，但是类不可以访问实例中的属性和方法，实例中的属性和方法需要实例化后才能调用和访问，但类依然不可以访问和调用方法)

## 属性
属性包括：实例属性和类属性，他们在定义和使用中有所区别，而最本质的区别是内存中保存的位置不同
- 实例属性属于对象,创建对象后可访问
- 类属性属于类,类和对象都可访问
- 私有属性属于类,外面是不能访问,只能在类中访问

应用场景： 通过类创建对象时，如果每个对象都具有相同的属性，那么就使用类属性
- 类属性在内存中只保存一份
- 实例属性在每个对象中都要保存一份
```
class Province():
 
    # 类属性
    country ＝ '中国'

    # 私有属性
    __city = '北京'
 
    def __init__(self, name):
 
        # 实例属性
        self.name = name
 
 
# 实例属性需要类实例化,然后通过对象访问
obj = Province('河北省')
print(obj.name)
 
# 直接访问类属性,访问类属性则不需要实例化,对象也可访问
print(Province.country)
print(obj.country)

# 私有属性是不能够访问的,只能类里面调用,这样会报错
print(Province.__city)
print(obj.__city)
```

## 方法

方法包括：普通方法、静态方法和类方法,三种方法在内存中都归属于类,区别在于调用方式不同。
- 普通方法：由对象调用,至少一个self参数,执行普通方法时,自动将调用该方法的对象赋值给self,self是实例的变量名(类不能调用实例的方法)
- 静态方法：由类调用,默认无参数,可以任意参数,无需创建对象即可调用(对象也能调用)
- 类方法：  由类调用,至少一个cls参数,执行类方法时,自动将cls传进类方法中,cls是当前类名,类方法和静态方法没什么差别,只是参数区别(对象也能调用)
```
class Province:
    country = "中国"
 
    def __init__(self,name):
        self.name = name
 
    def show(self):
        """普通方法，由对象调用执行（方法属于类）,实例化才能调用"""
        print(self.name)
 
    @staticmethod
    def f1(arg1,arg2):
        """静态方法，由类调用执行,可以没有参数，或者任意参数"""
        print(arg1,arg2)
 
    @classmethod
    def f2(cls):
        """类方法至少要有cls一个参数,cls就是类名，python自动会传，就像self"""
        print(cls)
 
obj = Province('python')  # 类实例化成对象
print(obj.name)           # 通过对象访问实例属性
obj.show()                # 通过对象执行实例方法
 
Province.f1(1111,2222)    # 静态方法，通过类调用
Province.f2()             # 类方法，通过类调用
 
obj.f1('python','linux')  # 对象也能调用静态方法
obj.f2()                  # 对象也能调用类方法
```
## 包装

包装是将方法包装成属性，属性通过对象调用，包装后的方法也是通过一样的方式调用，并且无需()

#### 1. 第一种使用包装的方法(使用@property)
```
class Pager():
 
    def __init__(self,all_count):
        self.all_count = all_count
 
    @property
    def all_pager(self):
        a1,a2 = divmod(self.all_count,10)
        if a2 == 0:
            return a1
        else:
            return a1 + 1
 
    @all_pager.setter
    def all_pager(self,value):
        print(value)
 
    @all_pager.deleter
    def all_pager(self):
        print('del all_page')
 
 
p = Pager(101)
ret = p.all_pager   # 执行这一句就会执行@property对应的方法
print(ret)
p.all_pager = 115   # 执行这一句赋值操作,就会执行@all_pager.setter对应的方法
del p.all_pager     # 执行这一句赋值操作,就会执行@all_pager.deleter对应的方法
```
#### 2. 第一种使用包装的方法(property())
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
result = p.foo       # 自动调用第一个参数中定义的方法：f1方法,result用于接收返回值
print(result)
 
p.foo = "python"     # 自动调用第二个参数中定义的方法：f2方法，并将"python"当作参数传入
 
del p.foo            # 自动调用第二个参数中定义的方法：f3方法
 
p.foo.__doc__        # 自动获取第四个参数中设置的值：description...
```
#### 3. 例子

[具有分页功能的包装使用](https://github.com/xiaozhiqi2000/learn_python/blob/master/day12/.gameClassgerClasspy)

## 类的特殊成员

上文介绍了Python的类成员以及成员修饰符，从而了解到类中有属性、方法和包装三大类成员，并且成员名前如果有两个下划线，则表示该成员是私有成员，私有成员只能由类内部调用。无论人或事物往往都有不按套路出牌的情况，Python的类成员也是如此，存在着一些具有特殊含义的成员，详情如下：
#### 1. \_\_doc__ 表示类的描述信息
```
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
 
    def func(self):
        pass
 
print(Foo.__doc__)
#输出：类的描述信息
```
#### 2. \_\_module__ 和  __class__ 
- __module__ 表示当前操作的对象在那个模块
- __class__     表示当前操作的对象的类是什么
```
lib/aa.py
class C:
 
    def __init__(self):
        self.name = "python"

index.py
from lib.aa import C
 
obj = C()
print obj.__module__     # 输出 lib.aa，即：输出模块
print obj.__class__      # 输出 lib.aa.C，即：输出类
```
#### 3. \_\_init__ 构造方法，通过类创建对象时，自动触发执行。
```
class Foo():
 
    def __init__(self, name):
        self.name = name
        self.age = 18
 
 
obj = Foo('python') # 自动执行类中的 __init__ 方法
```
#### 4. \_\_del__  析构方法，当对象在内存中被释放时，自动触发执行。

注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的
```
class Foo:
 
    def __del__(self):
        pass
```
#### 5. \_\_call__ 对象后面加括号，触发执行。

注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
```
class Foo:
 
 
    def __init__(self,name,age):
        print('init')
        self.name = name
        self.age = age
 
    def __call__(self, *args, **kwargs):
        print("call")
 
 
obj = Foo('python',27)
obj()                      # 对象() 会执行类中__call__方法
Foo('python',27)() # 这一句相当于上两句
```
#### 6. \_\_dict__ 类或对象中的所有成员

上文中我们知道：类的普通字段属于对象；类中的静态字段和方法等属于类
```
class Province():
 
    country = 'China'
 
    def __init__(self, name, count):
        self.name = name
        self.count = count
 
    def func(self, *args, **kwargs):
        print 'func'
 
# 获取类的成员，即：类属性、方法、
print(Province.__dict__)
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}
 
obj1 = Province('HeBei',10000)
print(obj1.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'HeBei'}
 
obj2 = Province('HeNan', 3888)
print(obj2.__dict__)
# 获取 对象obj2 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}
```
#### 7. \_\_str__ 如果一个类中定义了\_\_str__方法，那么在打印 对象 时，默认输出该方法的返回值
```
class Foo:
 
    def __init__(self,name,age):
        print('init')
        self.name = name
        self.age = age
 
    def __str__(self):  # 将实例化对象友好的输出
        return "%s - %d" %(self.name,self.age)
 
obj1 = Foo('tom',73)
obj2 = Foo('jerry',90)
print(obj1)
print(obj2)
 
ret = str(obj1)
print(type(ret),ret)
 
ret = obj1 + obj2
print(ret)
```
#### 8. \_\_getitem__、\_\_setitem__、\_\_delitem__ 用于索引操作，如字典。以上分别表示获取、设置、删除数据
```
class Foo():
    def __init__(self,name,age):
        print('init')
        self.name = name
        self.age = age
 
 
    def __getitem__(self, item):
        return 123
 
    def __setitem__(self, key, value):
        print('setitem')
 
    def __delitem__(self, key):
        print('del item')
 
obj = Foo('python',27)
 
 
ret = obj['ad']   # 自动触发执行 __getitem__
print(ret)
 
obj['k1'] = 111   # 自动触发执行 __setitem__
 
del obj['k1']     # 自动触发执行 __delitem__
```
#### 9. \_\_getslice__、\_\_setslice__、\_\_delslice__(此方法只适用于python2.x)该三个方法用于分片操作，如：列表
```
class Foo(object):
  
    def __getslice__(self, i, j):
        print '__getslice__',i,j
  
    def __setslice__(self, i, j, sequence):
        print '__setslice__',i,j
  
    def __delslice__(self, i, j):
        print '__delslice__',i,j
  
obj = Foo()
  
obj[-1:1]                   # 自动触发执行 __getslice__
obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
del obj[0:2]                # 自动触发执行 __delslice__
```
python3.x依然使用\_\_getitem__、\_\_setitem__、__delitem__
```
class Foo:
 
 
    def __init__(self,name,age):
        print('init')
        self.name = name
        self.age = age
 
 
    def __getitem__(self, item):
        print(item.start)
        print(item.stop)
        print(item.step)
 
        return 123
 
    def __setitem__(self, key, value):
        print(type(key),type(value))
 
    def __delitem__(self, key):
        print(type(key))
 
obj = Foo('python',27)
 
# 语法对应关系,将'ad'赋值给__getitem__中的item
 
ret2 = obj[1:4:2]
 
obj[1:4] = [11,22,33,44,55]
 
del obj[1:4]　
```
#### 10. \_\_iter__ 用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 __iter__ 
```
class Foo(object):
 
    def __init__(self, sq):
        self.sq = sq
 
    def __iter__(self):
        return iter(self.sq)
 
obj = Foo([11,22,33,44])
 
for i in obj:
    print(i)

或者使用yeild生成器
class Foo(object):
 
    def __init__(self, sq):
        self.sq = sq
 
    def __iter__(self):
        return iter(self.sq)
 
obj = Foo([11,22,33,44])
 
for i in obj:
    print(i)
```
#### 11. \_\_new__ 和 \_\_metaclass__
```
class Foo(object):
  
    def __init__(self):
        pass
  
obj = Foo()   # obj是通过Foo类实例化的对象

print type(obj) # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
print type(Foo) # 输出：<type 'type'>              表示，Foo类对象由 type 类创建
```
上述代码中，obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象。

如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，那么Foo类对象应该也是通过执行某个类的 构造方法 创建。

所以，obj对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，即：Foo类对象 是通过type类的构造方法创建。

那么，创建类就可以有两种方式：
```
a). 普通方式
class Foo(object):
  
    def func(self):
        print 'hello python'

b).特殊方式（type类的构造函数）
def func(self):
    print 'hello wupeiqi'
  
Foo = type('Foo',(object,), {'func': func})

#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员
＝＝》 类 是由 type 类实例化产生
```
那么问题来了，类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？

答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，所以，我们可以为 __metaclass__ 设置一个type类的派生类，从而查看 类 创建的过程。
```
class MyType(type):
 
    def __init__(self, what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)
 
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
 
        self.__init__(obj)
 
class Foo(object):
 
    __metaclass__ = MyType
 
    def __init__(self, name):
        self.name = name
 
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
 
# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo()
```
