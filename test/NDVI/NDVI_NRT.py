#!/usr/bin/python
# -*- coding=utf-8 -*-
#通过给定数据的日期，获取对应的 NRT lerc2 (v3) 数据


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def NRT():
    u = "https://api.gagogroup.cn/api/v3/nrt/"
    year = "2017/"
    month = "1/"
    day = "1/"
    z = "3/"
    x = "0/"
    y = "2"
    url = u + year + month + day + z + x + y
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    r = requests.get(url, headers=header)
    print r.content
    print r.url

if __name__ == "__main__":
    NRT()
