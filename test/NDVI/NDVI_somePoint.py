#!/usr/bin/python
# -*- coding=utf-8 -*-
#获取某个点的 NDVI 


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def some_point():
    lon = "145.5"
    lat = "27.5"
    start_date = "2016"
    end_date = "2017"
    url = "https://api.gagogroup.cn/api/v3/ndvi/values"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    param = {"lon":lon,"lat":lat,"from_date":start_date,"to_date":end_date}
    r = requests.get(url, headers=header, params=param)
    print r.content
    print r.url

if __name__ == "__main__":
    some_point()
