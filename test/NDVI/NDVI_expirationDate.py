#!/usr/bin/python
# -*- coding=utf-8 -*-
#NDVI 的有效日期是有间隔的，通过该接口可以获取有效的 NDVI 日期。


import json
import sys
sys.path.append(r'c:\python27\test\user')

import requests

import login_api

def expirationDate():
    year = "2017"
    url = "https://api.gagogroup.cn/api/v3/ndvi/dates"
    header = {"token":login_api.login()}
    header['content-type'] = "application/json"
    param = {'year': year}
    r = requests.get(url, headers=header, params=json.dumps(param) ,verify=False)
    print r.content

if __name__ == "__main__":
    expirationDate()
