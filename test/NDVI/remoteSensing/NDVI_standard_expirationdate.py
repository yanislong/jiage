#!/usr/bin/python
# -*- coding=utf-8 -*-
#获取某个点的 NDVI 


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def standard_expirationdate():
    year = [2017]
    url = "https://api.gagogroup.cn/api/v3/rs/modis/std/ndvi/dates"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    param = {"years":year}
    r = requests.get(url, headers=header, params=param)
    print r.content
    print r.url

if __name__ == "__main__":
    standard_expirationdate()
