#!/usr/bin
# -*- coding=utf-8 -*-
#通过给定的站点id, 年份, 月份, 请求的极值类型，获取该站点的某年极值温度天数


import sys
sys.path.append(r'c:\python27\gg\test\user')
import json

import requests

import login_api


class weather():
    head = ""

    def __init__(self):
        self.head = {"token":login_api.login()}
        print self.head
    
    def annual_dry_days(self):
        sid = '57315'
        y = '2017'
        m = [1]
        t = 'tmp'
        url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_dry_days"    
        param = {"stid":sid, "years":y}
        r = requests.get(url, headers=self.head, params=param, verify=False)
        print r.content
        print r.url

    def annual_avg_sunlight_hours(self):
        sid = '57315'
        y = '2017'
        m = [1]
        t = 'tmp'
        url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_average_sunlight_hours"    
        param = {"stid":sid, "years":y}
        r = requests.get(url, headers=self.head, params=param, verify=False)
        print r.content
        print r.url
        
    def annual_max_sunlight_hours(self):
        sid = '57315'
        y = '2017'
        m = [1]
        t = 'tmp'
        url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_max_sunlight_hours"    
        param = {"stid":sid, "years":y, "months":m}
        r = requests.get(url, headers=self.head, params=param, verify=False)
        print r.content
        print r.url

    def monthly_sunlight_hours_sum(self):
        sid = '57315'
        y = '2017'
        m = [1]
        t = 'tmp'
        url = "https://api.gagogroup.cn/api/v3/weather/analysis/monthly_sunlight_hours_sum"    
        param = {"stid":sid, "years":y, "months":m}
        r = requests.get(url, headers=self.head, params=param, verify=False)
        print r.content
        print r.url
        
    def annual_max_sunlight_hours(self):
        sid = '57315'
        y = '2017'
        m = [1]
        t = 'tmp'
        url = "https://api.gagogroup.cn/api/v3/weather/analysis/annual_max_sunlight_hours"    
        param = {"stid":sid, "years":y, "months": m}
        r = requests.get(url, headers=self.head, params=param, verify=False)
        print r.content
        print r.url
    
    
    
    

if __name__ == "__main__":
    w = weather()
#    w.annual_dry_days()
 #   w.annual_avg_sunlight_hours()
#    w.annual_max_sunlight_hours()
    w.monthly_sunlight_hours_sum()
