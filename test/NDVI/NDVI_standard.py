#!/usr/bin/python
# -*- coding=utf-8 -*-
#通过给定的站点id, 年份, 月份, 返回各年份给定月份的均温, 如果月份为全部12个月，获取该地区的各年均温


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def standard():
    sid = "57315"
    year = [2016,2017]
    month = [1,2,3]
    t = "tmp"
    url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_average_temperature"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    param = {"stid":sid,"years":year,"months":month,'type':t}
    r = requests.get(url, headers=header, params=param)
    print r.content
    print r.url

if __name__ == "__main__":
    standard()
