# -*- coding=utf-8 -*-
#NDVI底图数据

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def stand_mapdata():
    u = "https://api.gagogroup.cn/api/v3/rs/modis/nrt/ndvi/"
    year = "2017/"
    month = "4/"
    day = "25/"
    z = "0/"
    x = "0/"
    y = "0"
    url =  u + year + month + day + z + x + y
    header = {"token":login_api.login()}
    r = requests.get(url, headers=header, verify=False)
    print r.content

if __name__ == "__main__":
    stand_mapdata()
