from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://news.baidu.com')
driver.maximize_window()
time.sleep(2)

#打印所有图片大小
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.size)

driver.quit()
