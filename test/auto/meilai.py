#!/usr/bin/python
#-*- coding=utf-8 -*-

import time

from selenium import webdriver

urls = ['window.open("http://demo.gagogroup.cn/meilai-project/#/GroundPreview/")','window.open("http://demo.gagogroup.cn/meilai-project/#/GroundList/")',\
        'window.open("http://demo.gagogroup.cn/meilai-project/#/FarmShow/")','window.open("http://demo.gagogroup.cn/meilai-project/#/FarmList/")',\
        'window.open("http://demo.gagogroup.cn/meilai-project/#/WeatherInfo/")','window.open("http://demo.gagogroup.cn/meilai-project/#/CropGrowth")',\
        'window.open("http://demo.gagogroup.cn/meilai-project/#/RadarInfo")']
driver = webdriver.Chrome()
driver.get('http://demo.gagogroup.cn/meilai-project')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('sunliang')
driver.find_element_by_name('old').send_keys('sunliang')
driver.find_element_by_tag_name('button').click()
time.sleep(5)
driver.find_element_by_tag_name('svg').click()
time.sleep(2)
i = 0
for link in driver.find_elements_by_xpath('//*[@style]'):
    i += 1
#    print link.get_attribute('style')
    if i == 22:
        print link.text
        link.click()
        time.sleep(3)
        break
j = 1
for u in urls:
    print u
    driver.execute_script(u)
    driver.switch_to_window(driver.window_handles[j])
    time.sleep(10)
    j += 1
'''
driver.find_element_by_tag_name('svg').click()
i = 0
for link in driver.find_elements_by_xpath('//*[@style]'):
    if i == 20:
        print link.text
        link.click()
        time.sleep(5)
        break
i = 0
driver.find_element_by_tag_name('svg').click()
for link in driver.find_elements_by_xpath('//*[@style]'):
    if i == 18:
        print link.text
        link.click()
        time.sleep(5)
        break

i=1
for link in driver.find_elements_by_xpath('//*[@data-name]'):
#    print link.get_attribute('data-name')
    if i == 1:
        link.click()
    i += 1
time.sleep(2)
'''
driver.quit()
