from selenium import webdriver
import time
import re

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://home.baidu.com/home/index/contact_us')
time.sleep(2)

#得到页面源代码
doc = driver.page_source
#利用正则，得出emails列表
emails = re.findall(r'[\w]+@[\w\.-]+',doc)

#循环打印邮箱
for email in emails:
    print(email)

