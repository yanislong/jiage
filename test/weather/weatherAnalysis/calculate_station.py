#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的经纬度, 返回距离该点最近的站点id

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def calculate_station():
    x = '30'
    y = '120'
    url = "https://api.gagogroup.cn/api/v3/weather/analysis/calculate_station"
    header = {"token":login_api.login()}
    param = {"alt":'30',"lon":'120'}
    r = requests.get(url, headers=header, params=param, verify=False)
    print r.content
    print r.url
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    calculate_station()
