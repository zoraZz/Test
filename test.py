# -*- coding:utf-8 -*-
from selenium import webdriver
import time


# 时间格式进行格式化
def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.get_screenshot_as_file("截图\\" + time_format() + ".png")

time.sleep(2)
driver.quit()
