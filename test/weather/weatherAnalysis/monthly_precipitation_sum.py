#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的站点id, 年份, 月份, 请求的极值类型，获取该站点的某年极值温度天数


import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def monthly_precipitation_sum():
    sid = '57315'
    y = '2017'
    m = [1]
    t = 'tmp'
    url = "https://api.gagogroup.cn/api/v3/weather/analysis/monthly_precipitation_sum?"
    header = {"token":login_api.login()}
    param = {"stid":sid, "years":y, "months":m}
    r = requests.get(url, headers=header, params=param, verify=False)
    print r.content
    print r.url
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    monthly_precipitation_sum()
