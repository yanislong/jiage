#!/usr/bin
# -*- coding=utf-8 -*-
#气象实时数据、预测数据、历史数据相关接口，请注意，所以的接口时间默认为 UTM+8 时区
#根据经纬度获取数字高程模型

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def number_dem():
    x = 19.99
    y = 86
    url = "https://api.gagogroup.cn/api/v3/weather/dem"
    param = {"lat":x, "lon":y}
    header = {"token":login_api.login()}
    r = requests.get(url, params=param, headers=header, verify=False)
    print r.content

if __name__ == "__main__":
    number_dem()
