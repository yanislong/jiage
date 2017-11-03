#！/usr/bin/python
# -*- coding=utf-8 -*-
#获取用户信息

import sys
sys.path.append(r'c:\python27\test\user')
import json

import requests

import login_api

def user_info():
    oldpassword = "aletan"
    newpassword = "aletan"
    url = "https://api.gagogroup.cn/api/v3/user_info"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    data = {"oldPassword":oldpassword,"newPassword":newpassword}
    r = requests.get(url, headers=header)
    print r.content

if __name__ == "__main__":
    user_info()
