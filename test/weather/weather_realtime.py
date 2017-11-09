#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的经纬度，获取该地区的实时气温，湿度，天气情况,
#首先访问高德地图天气接口，访问失败再从本地查询。无数据的项置为null

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def realtime():
    x = '30'
    y = '120'
    url = "https://api.gagogroup.cn/api/v3/weather/realtime"
    header = {"token":login_api.login()}
    param = {"alt":'30',"lon":'120'}
    r = requests.get(url, headers=header, params=param, verify=False)
    print r.content
    print r.url
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    realtime()
