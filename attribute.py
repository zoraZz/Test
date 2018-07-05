from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

#获取所有有href属性的值
for link in driver.find_elements_by_xpath('//*[@href]'):
    print(link.get_attribute('type'))  #也可以打印其他的属性值，比如id/title/size 等等

driver.quit()