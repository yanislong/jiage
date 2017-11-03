import requests
import json

url = "http://api.gagogroup.cn/api/v3/ndvi/dates?years=2017"
header = {"token":"c81c96779c41177fee3f14ef114128956fc17310c4591f194db6b67cfe30c1c1c296ebeddf5bb73ccd5a6aca542b919c"}
r = requests.get(url, headers=header)
print r.content
