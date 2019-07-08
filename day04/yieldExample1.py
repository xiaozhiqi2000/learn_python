#!/usr/bin/env python
#-*- coding:utf-8 -*-


def get_list_page(itemlist, chunksize=2000):
    """
    分页列表
    :param itemlist:
    :param chunksize:
    :return:
    """
    while chunksize < len(itemlist):
        yield itemlist[0:chunksize]
        itemlist = itemlist[chunksize:]
    yield itemlist


uid_list = ['35473084', '35519740', '34971566', '36146728', '35489551', '36257465', '35580556', '35891354', '35412733', '35937052', '31132569', '34568489', '36326720', '35577719', '35091008', '32280276', '35263216', '33302721']


items = get_list_page(uid_list,chunksize=3)
for item in items:
    print(item)
