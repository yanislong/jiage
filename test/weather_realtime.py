# -*- coding=utf-8 -*-
#通过给定的经纬度，获取该地区的实时气温，湿度，天气情况, 首先访问高德地图天气接口，访问失败再从本地查询。无数据的项置为null

import requests
import json

url = "https://api.gagogroup.cn/api/v3/weather/realtime"
param = {"lat":0, "lon":-90}
header = {"token":"f4eb4a8119a563339678bf7f6f6de0b9804682ddbb3443f6b0959ba42139906e20febf772efd33cebbee7f04439792bb"}
r = requests.get(url, params=param, headers=header)
print r.content
