#！/usr/bin/python
# -*- coding=utf-8 -*-
#获取用户信息

import sys
sys.path.append(r'c:\python27\test\user')
import json

import requests

import login_api

def edit_user_info():
    phoneNumber = "13112341234"
    telephone = "13143214321"
    name = "aletan"
    url = "https://api.gagogroup.cn/api/v3/user_info"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    data = {"oldPhoneNumber":phoneNumber,"newTelephone":telephone,"newUsername":name}
    r = requests.put(url, headers=header, data=json.dumps(data))
    print r.content

if __name__ == "__main__":
    edit_user_info()
