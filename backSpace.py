from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

#定位输入框
element = driver.find_element_by_id('kw')
element.send_keys('selenium')
time.sleep(1)
#全选
element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
#回退键删除
element.send_keys(Keys.BACKSPACE)
time.sleep(1)

driver.quit()