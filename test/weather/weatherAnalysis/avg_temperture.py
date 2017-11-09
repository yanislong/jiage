#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的站点id, 年份, 月份, 返回各年份给定月份的均温,
#如果月份为全部12个月，获取该地区的各年均温

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def avg_temperture():
    sid = '57315'
    y = '2017'
    m = [1]
    t = 'tmp'
    url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_average_temperature"
    header = {"token":login_api.login()}
    param = {"stid":sid, "years":y, "months":m, "type":t}
    r = requests.get(url, headers=header, params=param, verify=False)
    print r.content
    print r.url
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    avg_temperture()
