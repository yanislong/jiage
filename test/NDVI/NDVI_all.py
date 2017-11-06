#!/usr/bin/python
# -*- coding=utf-8 -*-
#获取某个点的 NDVI 


import json
import sys
sys.path.append(r'c:\python27\test\user')
sys.path.append(r'c:\python27\gg\test\NDVI')

import requests

import login_api
import NDVI_expirationDate
import NDVI_somePoint
import NRT_lerc
import standard_lerc

def nrt_lerc():
    year = "2016/"
    month = "1/"
    day = "1/"
    z = "3/"
    x = "0/"
    y = "2/"
    u = "https://api.gagogroup.cn/api/v3/nrt/"
    url = u + year + month + day + z + x + y
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    r = requests.get(url, headers=header)
    print r.content
    print r.url

if __name__ == "__main__":
    print ">>>>>>>>>>>>>>>>>>>>>>>"
    NDVI_expirationDate.expirationDate()
    print ">>>>>>>>>>>>>>>>>>>>>>>"
    NDVI_somePoint.some_point()
    print ">>>>>>>>>>>>>>>>>>>>>>>"
    NRT_lerc.nrt_lerc()
    print ">>>>>>>>>>>>>>>>>>>>>>>"
    standard_lerc.stand_lerc()
