from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('http://www.baidu.com')
time.sleep(2)

driver.find_element_by_link_text('新闻').click()
time.sleep(2)

#浏览器上前面和后退操作
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.quit()