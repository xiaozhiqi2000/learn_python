# 今天主要内容
1. [反射](https://github.com/xiaozhiqi2000/learn_python/tree/master/day07#json%E6%A8%A1%E5%9D%97)
2. [异常处理](https://github.com/xiaozhiqi2000/learn_python/tree/master/day07#pickle%E6%A8%A1%E5%9D%97)
3. [模块中特殊变量](https://github.com/xiaozhiqi2000/learn_python/tree/master/day07#xml%E6%A8%A1%E5%9D%97)

## 反射

python中的反射功能是由以下四个内置函数提供
- hasattr 检查是否含有某成员
- getattr 获取成员
- setattr 设置成员
- delattr 删除成员
以字符串方式导入模块
- __import__()
- importlib() 推荐使用
#### 1. 以伪造Web框架的路由系统举例(执行脚本和模块在同一目录)
├── account.py
├── home.py
├── index.py
└── README.md
```
#!/usr/bin/env python
#-*- coding:utf8 -*-

def run():
    inp = input("请输入URL:>>>")

    m, f = inp.strip().split("/")

# 第一种方法
    obj = __import__(m)      
    if hasattr(obj,f):
        func = getattr(obj,f)
        func()
    else:
        print(404)

# 第二种方法
    # import importlib
    # import importlib.util
    #result = importlib.util.find_spec("lib." + m)
    #if result:
    #    obj = importlib.import_module(m)
    #    if hasattr(obj,f):
    #        func = getattr(obj,f)
    #        func()
    #    else:
    #        print(404)
    #else:
    #    print(404)

if __name__ == "__main__":
    run()

#执行 python index.py 输入home/home或者account/login就会执行home.py中的home()方法，就会执行account.py中的login()方法
```
#### 2. 以伪造Web框架的路由系统举例(执行脚本和模块在不同一目录)
├── index.py
├── lib
│   ├── account.py
│   └── home.py
└── README.md
```
#!/usr/bin/env python
#-*- coding:utf8 -*-

def run():
    inp = input("请输入URL:>>>")

    m, f = inp.strip().split("/")
    try:
        obj = __import__("lib." + m,fromlist=True)
        if hasattr(obj,f):
            func = getattr(obj,f)
            func()
        else:
            print(404)
    except:
        print(404)

# 第二种方法
#    import importlib
#    import importlib.util

#    result = importlib.util.find_spec("lib." + m)
#    if result:
#        obj = importlib.import_module("lib." + m)
#        if hasattr(obj,f):
#            func = getattr(obj,f)
#            func()
#        else:
#            print(404)
#    else:
#        print(404)


if __name__ == "__main__":
    run()

#执行 python index1.py 输入home/home或者account/login就会执行lib.home.py中的home()方法，就会执行lib.account.py中的login()方法
```
## 异常处理

### python异常是一个对象，表示错误或意外情况
1. 在python检测到一个错误时，将触发一个异常
- python可以通常异常传导机制传递一个异常对象，发出一个异常情况出现的信号
- 程序员也可以在代码中手动触发异常
2. python异常也可以理解为：程序出现了错误而在正常控制流以外采取的行为
- 第一阶段：解释器触发异常，此时当前程序流将被打断
- 第二阶段：异常处理，如忽略非致命错误、减轻错误带来的影响等

### 异常处理语法:
```
try:
    # 主代码块
    pass
except Exception as e:
    # 异常时，执行该块, python2 except Exception,e
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass
```
### 常见的异常错误
```
AssertionError: 断言语句失败
AttributeError: 属性引用或赋值失败
FloatingPointError: 浮点型运算失败
IOError:  I/O操作失败
ImportError: import语句不能找到要导入的模块，或者不能找到该模块特别请求的名称
IndentationError: 解析器遇到了一个由于错误的缩进而引发的语法错误
IndexError: 用来索引序列的证书超出了范围
KeyError: 用来索引映射的键不再映射中
keyboardInterrupt: 用户按了中断键(Ctrl+c,Ctrl+Break或Delete键)
MemoryError: 运算耗尽内存
NameError: 引用了一个不存在的变量名
NotImplementedError: 由抽象基类引发的异常，用于指示一个具体的子类必须覆盖一个方法
OSError: 由模块os中的函数引发的异常，用来指示平台相关的错误
OverflowError: 整数运算的结果太大导致溢出
SyntaxError: 语法错误
SystemError: python本身或某些扩展模块中的内部错误
TypeError：对某对象执行了不支持的操作
UnboundLocalError：引用未绑定值的本地变量
UnicodeError：在Unicode的字符串之间进行转换时发生的错误
ValueError：应用于某个对象的操作或函数，这个对象具有正确的类型，但确有不适当的值
WindowsError：模块os中的函数引发的异常，用来指示与WIndows相关的错误
ZeroDivisionError： 除数为0
```
### 主动触发异常
```
try:
    raise Exception('错误了。。。')
except Exception as e:
    print(e)
```
### 自定义异常
```
class MyException(Exception):
  
    def __init__(self, msg):
        self.message = msg
  
    def __str__(self):
        return self.message
  
try:
    raise MyException('我的异常')
except WupeiqiException as e:
    print(e)
```
### 断言
```
# assert 条件
  
assert 1 == 1
  
assert 1 == 2
```













