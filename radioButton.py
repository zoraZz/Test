from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://news.baidu.com/')
driver.maximize_window()
time.sleep(2)

radios = driver.find_elements_by_xpath('//*[@type="radio"]')
time.sleep(2)

for i in radios:
    i.click()