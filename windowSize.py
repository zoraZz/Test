from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 全屏
driver.maximize_window()
time.sleep(1)
print(driver.get_window_size())

#设置浏览器窗口大小
driver.set_window_size(1280,800)     #分辨率 1280*800
time.sleep(1)
print(driver.get_window_size())

driver.set_window_size(1024,768)     #分辨率 1024*768
time.sleep(1)
print(driver.get_window_size())

driver.quit()