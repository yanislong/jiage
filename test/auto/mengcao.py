#!/usr/bin/python
#-*- coding=utf-8 -*-

import time

from selenium import webdriver

urls = [['window.open("http://demo.gagogroup.cn/mengcao-img/#/GagoView/")',r'GagoView'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/TianRan/")',r'TianRan'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/CropGrowth")',r'CropGrowth'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/NaturalYield")',r'NaturalYield'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/ArtificialYield")',r'ArtificialYield'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/Desertification")',r'Desertification'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/Degeneration")',r'Degeneration'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/Salinization")',r'Salinization'],\
        ['window.open("http://demo.gagogroup.cn/mengcao-img/#/Coverage")',r'Coverage']]
t = 5
driver = webdriver.PhantomJS(executable_path=r"C:\Users\long\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#driver = webdriver.Chrome()
driver.get('http://demo.gagogroup.cn/mengcao-img/#/GagoView')
driver.maximize_window()
#driver.find_element_by_name('username').send_keys('sunliang')
#driver.find_element_by_name('old').send_keys('sunliang')
#driver.find_element_by_tag_name('button').click()
time.sleep(2)
#print driver.page_source
 
j = 1
for u in urls:
    print u
    driver.execute_script(u[0])
    driver.switch_to_window(driver.window_handles[j])
    time.sleep(t)
    driver.find_element_by_class_name('ant-select-arrow').click()
    k = 1
    for link in driver.find_elements_by_xpath('//*[@role="menuitem"]'):
#        print link.location
        if k == 2:
            time.sleep(1)
        k += 1
   # driver.execute_script('<script>alert(123)</script>')
#    driver.get_screenshot_as_file('c:\\users\\long\\Desktop\\img\\' + str(j) + '.png')
    driver.save_screenshot('c:\\users\\long\\Desktop\\img\\' + u[1] + '.png')
    j += 1
driver.quit()
