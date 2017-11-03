# -*- coding=utf-8 -*-
#气象实时数据、预测数据、历史数据相关接口，请注意，所以的接口时间默认为 UTM+8 时区

import requests
import json

url = "https://api.gagogroup.cn/api/v3/weather/dem"
param = {"lat":19.99,"lon":86}
header = {"token":"f4eb4a8119a563339678bf7f6f6de0b9804682ddbb3443f6b0959ba42139906e20febf772efd33cebbee7f04439792bb"}
r = requests.get(url, params=param, headers=header)
print r.content
