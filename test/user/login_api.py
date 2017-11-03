#!/usr/bin/python
#-*-coding=utf-8 -*-

import json
import re

import requests

def login():
    name = "aletan"
    pawd = "aletan"
    url = "https://api.gagogroup.cn/api/v3/login"
    header = {"Content-Type":"application/json"}
    data = {"username":name, "password":pawd}
    r = requests.post(url, data=json.dumps(data), headers=header)
#    print r.content
    l1 = re.compile(r'"token":"(.*?)"')
    l2 = l1.findall(r.content)
#    print l2
    return l2[0]

if __name__ == "__main__":
    login()
