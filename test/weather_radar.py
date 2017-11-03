# -*- coding=utf-8 -*-
#通过传递给服务器想要获取的图片的时间,返回图片数据

import requests
import json

url = "https://api.gagogroup.cn/api/v3/weather/radar"
param = {"time":201611161010}
header = {"token":"f4eb4a8119a563339678bf7f6f6de0b9804682ddbb3443f6b0959ba42139906e20febf772efd33cebbee7f04439792bb"}
r = requests.get(url, params=param, headers=header)
with open(r'd:\123.png', 'wb') as f:
    f.write(r.content)
print r.content
