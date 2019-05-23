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
