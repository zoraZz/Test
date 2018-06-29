from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
time.sleep(1)

#第一种断言，常用
try:
    assert '百度一下' in driver.title
    print('Test passed')
except Exception as e:
    print('Test failed',format(e))

#第二种断言
# if '百度一下，你就知道' == driver.title:
#     print('Test passed')
# else:
#     print('Test failed')

driver.quit()