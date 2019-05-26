#!/usr/bin/env python
# -*- coding:utf-8 -*-

# #####################  定义实现功能的类  #####################

class Person:

    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight =fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight = self.fight - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""
        
        self.fight = self.fight + 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""
        
        self.fight = self.fight - 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s"  % (self.name, self.gender, self.age, self.fight)
        print temp

        
# #####################  开始游戏  #####################

cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色

cang.incest() #苍井空参加一次多人游戏
dong.practice()#东尼木木自我修炼了一次
bo.grassland() #波多多参加一次草丛战斗


#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()


cang.incest() #苍井空又参加一次多人游戏
dong.incest() #东尼木木也参加了一个多人游戏
bo.practice() #波多多自我修炼了一次

#输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()
