#!/usr/bin/env python
#-*-coding:utf-8-*-
#用户交互，显示省市县三级联动的选择

dic = {
    "福建": {
        "龙岩": ["武平县", "上杭县", "连城县", "长汀县"],
        "福州": ["福清县", "闽侯县", "连江县", "罗源县"],
    },
    "广东": {
        "广州":["花都区", "番禺区", "天河区", "白云区"],
        "深圳":["南山区", "宝安区", "福田区", "罗湖区"]
    },
    "江西": {
        "上饶":["玉山县", "铅山县", "横峰县", "潘阳县"],
        "南昌":["南昌县", "安义县", "进贤县", "云浦县"]
    }
}
for k in dic.keys():
    print(k)
flag=True
while flag:
    n=input("请输入你所在省：")
    for k in dic.keys():
        if n in dic.keys():
            if k == n:
                for i in dic[n].keys():
                    print(i)
                w = input("请输入你所在的城市：")
                for i in dic[n].keys():
                    if w in dic[n].keys():
                        if i == w:
                            for k in dic[n][w]:
                                print(k)
                            s=input("请输入你所在的县：")
                            for j in dic[n][w]:
                                if s in dic[n][w]:
                                    if j==s:
                                        print("你所在的位置是：%s省%s市%s县" % (n,w,s))
                                        flag = False
                                        break
                                else:
                                    print('不存在，请重新输入')
                                    break
                    else:
                        print('不存在，请重新输入')
                        break
        else:
            print('不存在，请重新输入')
            break
