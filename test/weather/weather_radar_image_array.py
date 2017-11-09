#!/usr/bin
# -*- coding=utf-8 -*-
#返回图片数据信息,为稍后请求雷达图片准备。该接口为转发第三方网址数据，
#如果转发失败，会返回缓存的上一次（10分钟前）的数据

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def radar_image_array():
    url = "https://api.gagogroup.cn/api/v3/weather/radar_prepare"
    header = {"token":login_api.login()}
    r = requests.get(url, headers=header, verify=False)
    print r.content
    #with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
    #   f.write(r.content)

if __name__ == "__main__":
    radar_image_array()
