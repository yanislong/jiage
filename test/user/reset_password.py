#！/usr/bin/python
# -*- coding=utf-8 -*-
#重置密码

import sys
sys.path.append(r'c:\python27\test\user')
import json

import requests

import login_api

def reset_passwd():
    newpasswd = "aletan"
    url = "https://api.gagogroup.cn/api/v3/reset_password"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    data = {"newPassword":newpasswd}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

if __name__ == "__main__":
    reset_passwd()
