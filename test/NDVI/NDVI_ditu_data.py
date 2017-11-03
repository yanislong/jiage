# -*- coding=utf-8 -*-
#NDVI底图数据

import requests
import json

url = "https://api.gagogroup.cn/api/v3/rs/modis/std/ndvi/2016/1/1/3/0/2"
header = {"token":"6a2aa281ab73522e81c369dc3edf2cdf23244decf28d83deeb4c02301c7c79da3611b541046854e143d8233672ec7ef0"}
r = requests.get(url, headers=header, verify=False)
print r.content
