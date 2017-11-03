import time
from selenium import webdriver

obj = webdriver.PhantomJS(executable_path=r"C:\Users\long\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
obj.set_page_load_timeout(15)
try:
    obj.get('http://demo.gagogroup.cn/mengcao-img/#/GagoView')
    time.sleep(5)
    obj.save_screenshot('hello.png')
    print obj.title
 #   print obj.page_source
except Exception as e:
    print e

obj.quit()
