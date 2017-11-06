# -*- coding=utf-8 -*-
#NDVI底图数据

import sys
sys.path.append(r'c:\python27\gg\test\NDVI\remoteSensing')
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api
import NDVI_standard_expirationdate
import NDVI_standard_point_history
import NDVI_standard_mapdata
import NRT_stansard_mapdata
import NRT_colour_mapdata


def colour_mapdata():
    u = "https://api.gagogroup.cn/api/v3/rs/modis/nrt/true_color/ndvi/"
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
    print ">>>>>>>>>>>>>>>>>>>>"
    NDVI_standard_expirationdate.standard_expirationdate()
    print ">>>>>>>>>>>>>>>>>>>>"
    NDVI_standard_mapdata.standard_mapdata()
    print ">>>>>>>>>>>>>>>>>>>>"
    NDVI_standard_point_history.standard_point_history()
    print ">>>>>>>>>>>>>>>>>>>>"
    NRT_stansard_mapdata.stand_mapdata()
    print ">>>>>>>>>>>>>>>>>>>>"
    NRT_colour_mapdata.colour_mapdata()
