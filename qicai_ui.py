#!/usr/bin/python
# -*- coding=utf-8 -*-

import time

from selenium import webdriver
from scapy.all import *

from scapy.arch.windows import compatibility
from scapy.all import log_runtime, MTU, ETH_P_ALL, PcapTimeoutElapsed, plist

compatibility.log_runtime = log_runtime
compatibility.MTU = MTU
compatibility.PcapTimeoutElapsed = PcapTimeoutElapsed
compatibility.ETH_P_ALL = ETH_P_ALL
compatibility.plist = plist


#driver = webdriver.PhantomJS(executable_path='')
hailong = webdriver.Chrome()

def login():
    global hailong
    url = "http://beta.gagogroup.cn/test/colorful-forestry/#/login"
    hailong.get(url)
    hailong.maximize_window()
    time.sleep(2)
    hailong.find_element_by_css_selector("input[type='text']").send_keys('gagogl')
    hailong.find_element_by_css_selector('input[type="password"]').send_keys('gagogladmin')
    hailong.find_element_by_tag_name('button').click()
   # time.sleep(2)
    dpkt = sniff(filter="srcport 80", count=20)

    print dpkt
    wrpcap(r'demo.pcap', dpkt)

if __name__ == "__main__":
    login()
    hailong.quit()
