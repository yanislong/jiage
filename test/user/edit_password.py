#！/usr/bin/python
# -*- coding=utf-8 -*-
#修改密码

import sys
sys.path.append(r'c:\python27\test\user')
import json

import requests

import login_api

def edit_password():
    oldpassword = "aletan"
    newpassword = "aletan"
    url = "https://api.gagogroup.cn/api/v3/edit_password"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    data = {"oldPassword":oldpassword,"newPassword":newpassword}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

if __name__ == "__main__":
    edit_password()
