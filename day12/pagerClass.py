#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Pager():
     
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        try:
            p = int(current_page)
        except:
            p = 1
        self.current_page = p
        
        # 一页显示多少几条
        self.per_items = 10
 
    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val
 
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val
 

if __name__ == "__main__":
    while True:
        current_page = input("input your num>>>")
        obj = Pager(current_page)
        
        list_page = []
        for i in range(100):
            list_page.append(i)

        print(list_page[obj.start:obj.end])
        
