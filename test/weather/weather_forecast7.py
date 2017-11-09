#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的经纬度，获取该地区的实时气温，湿度，天气情况,
#首先访问高德地图天气接口，访问失败再从本地查询。无数据的项置为null

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def forecast():
    x = '30'
    y = '120'
    h = '2'
    f = 'tmp' #tmp: 温度， apcp: 降水，rh: 湿度, tmax: 最高温, tmin: 最低温, wnd_spd: 风速
    url = "https://api.gagogroup.cn/api/v3/weather/coordinate/forecast7"
    header = {"token":login_api.login()}
    param = {"alt":x, "lon":y, 'hrs':h, 'features':f}
    r = requests.get(url, headers=header, params=param, verify=False)
    print r.content
    print r.url
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    forecast()
