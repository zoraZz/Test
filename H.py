from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

#打开目标网址
driver = webdriver.Chrome()
driver.get('http://hjc.ibjhbet.net/')
driver.maximize_window()

#登录成功
driver.find_element_by_id('login_username').send_keys('vgnihaoa1')
driver.find_element_by_id('login_password').send_keys('123456')
driver.find_element_by_class_name('btn-login').click()
time.sleep(5)

#鼠标悬停
article = driver.find_element_by_id('member_name')
ActionChains(driver).move_to_element(article).perform()
time.sleep(5)
#点击“快速提款”
menu = driver.find_element_by_xpath('/html/body/header/div/ul/li[3]/a[1]')
menu.click()
time.sleep(5)

#关闭浏览器
driver.quit()