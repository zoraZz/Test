from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('http://www.baidu.com')
time.sleep(2)

#调用 .size，打印尺寸
buttonsize = driver.find_element_by_id('su')
print(buttonsize.size)

#全选
element = driver.find_element_by_tag_name('body')
element.send_keys(Keys.CONTROL + 'a')
