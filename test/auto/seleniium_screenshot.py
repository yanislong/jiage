#!/usr/bin/python
# -*- coding=utf-8 -*-
#获取某个点的 NDVI 


import json
import time
import sys
sys.path.append(r'c:\python27\test\user')

import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import login_api

def standard_mapdata():
    year = "2017/"
    month = '4/'
    day = "25/"
    z = "0/"
    x = "0/"
    y = "0"
    u = "https://api.gagogroup.cn/api/v3/rs/modis/nrt/ndvi/"
    url = u + year + month + day + z + x + y
#    url1 = "http://www.baidu.com"
    header = {"Content-Type":"application/json"}
    header['token'] = login_api.login() 
    dcap = dict(DesiredCapabilities.PHANTOMJS) 
    dcap['phantomjs.page.settings.token'] = '6bc7d7e26e1d1dc31b3823b4442514ee13bd5f8e957f936f8fb7ab1faf7e5fd5e38441865dd1ff0d9705e796a906d9ad' 
    dd = webdriver.PhantomJS(executable_path=r'C:\Users\long\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe',desired_capabilities=dcap)
    dd.get(url)
 #   dd.add_header({'name':'token','value':'6bc7d7e26e1d1dc31b3823b4442514ee13bd5f8e957f936f8fb7ab1faf7e5fd5e38441865dd1ff0d9705e796a906d9ad'})
    time.sleep(5)
    dd.save_screenshot(r'c:\users\long\Desktop\rizi.png')
    dd.quit()
    print 'hello'
    #r = requests.get(url, headers=header)
    #with open('c:\\users\long\\desktop\\tu.jpg','wb') as ff:
     #   ff.write(r.content)
    #print r.content
    #print r.url

if __name__ == "__main__":
    standard_mapdata()
