#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(5)

#方法一添加断言
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').is_displayed()
# print('测试通过')
# driver.quit()

#方法二添加断言
ele_string = driver.find_element_by_xpath('//*[@id="1"]/h3/a').text
if (ele_string == u'Selenium - Web Browser Automation'):
    print('测试通过')
    #打印浏览器版本
    print('当前浏览器版本是：',driver.capabilities['version'])
    #获取当前页面URL
    print('当前页面URL是：',driver.current_url)
    #获取当前页面的title
    print('当前页面title是：',driver.title)
else:
    print('测试失败')
driver.quit()

