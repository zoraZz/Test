from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.baidu.com')
time.sleep(2)
try:
    driver.find_element_by_link_text('新闻').click()
    # driver.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
    print('test passed:link text is found')
except Exception as e:
    print('test failed:link text is not found')

driver.quit()
