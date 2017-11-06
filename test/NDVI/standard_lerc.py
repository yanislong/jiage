#!/usr/bin/python
# -*- coding=utf-8 -*-
#获取某个点的 NDVI 


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def stand_lerc():
    year = "2016/"
    month = "1/"
    day = "1/"
    z = "3/"
    x = "0/"
    y = "2/"
    u = "https://api.gagogroup.cn/api/v3/ndvi/"
    url = u + year + month + day + z + x + y
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    r = requests.get(url, headers=header)
    print r.content
    print r.url

if __name__ == "__main__":
    stand_lerc()
