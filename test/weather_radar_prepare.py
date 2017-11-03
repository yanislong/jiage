# -*- coding=utf-8 -*-
#返回图片数据信息,为稍后请求雷达图片准备。该接口为转发第三方网址数据，如果转发失败，会返回缓存的上一次（10分钟前）的数据

import requests
import json

url = "https://api.gagogroup.cn/api/v3/weather/radar_prepare"
header = {"token":"f4eb4a8119a563339678bf7f6f6de0b9804682ddbb3443f6b0959ba42139906e20febf772efd33cebbee7f04439792bb"}
r = requests.get(url, headers=header)
print r.content
