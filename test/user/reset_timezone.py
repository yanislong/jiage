#！/usr/bin/python
# -*- coding=utf-8 -*-
#重置时区

import sys
sys.path.append(r'c:\python27\test\user')
import json

import requests

import login_api

def reset_timezone():
    newtimezone = 8
    url = "https://api.gagogroup.cn/api/v3/reset_timezone"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    data = {"newTimezone":newtimezone}
    r = requests.post(url, headers=header, data=json.dumps(data))
    print r.content

if __name__ == "__main__":
    reset_timezone()
