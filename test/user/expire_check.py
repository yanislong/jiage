#!/usr/bin/python
# -*- coding=utf-8 -*-
#验证session是否超时

import json
import sys
sys.path.append('c:\\python27\\test\\user')

import requests

import login_api

def check_timeout():
    url = "https://api.gagogroup.cn/api/v3/expire_check"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login()
    r = requests.post(url, headers=header)
    print r.content

if __name__ == "__main__":
    check_timeout()
