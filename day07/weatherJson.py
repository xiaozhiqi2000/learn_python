#!/usr/bin/env python
# coding: utf8

import requests, json

response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=深圳')
response.encoding="utf8"

dic = json.loads(response.text)
print(dic, type(dic))
