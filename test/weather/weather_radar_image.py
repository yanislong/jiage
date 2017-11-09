#!/usr/bin
# -*- coding=utf-8 -*-
#通过传递给服务器想要获取的图片的时间,返回图片数据

import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api

def radar_image():
    t = "201611161010"
    url = "https://api.gagogroup.cn/api/v3/weather/radar"
    param = {"time":t}
    header = {"token":login_api.login()}
    r = requests.get(url, params=param, headers=header, verify=False)
    print r.content
    with open(r'c:\users\long\Desktop\tttt.png','wb') as f:
        f.write(r.content)

if __name__ == "__main__":
    radar_image()
