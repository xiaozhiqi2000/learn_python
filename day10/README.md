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

