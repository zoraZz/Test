from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

try:
    driver.find_element_by_partial_link_text('主页').click()
    print('test passed')
except Exception as e:
    print('test failed')

driver.quit()