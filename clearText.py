from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(5)

try:
    #清除文本内容
    driver.find_element_by_id('kw').clear()
    #刷新当前页面
    driver.refresh()
    print('test passed')
except Exception as e:
    print('test failed',format(e))

# driver.quit()