from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
# time.sleep(5)

driver.get('https://www.baidu.com')
try:
    driver.find_element_by_id('kw')
    print('test passed')
except Exception as e:
    print('test failed',format(e))

driver.quit()