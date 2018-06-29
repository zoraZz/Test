from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)

#点击“登录”，弹出登录窗口
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(2)

#在登录窗口中选择“用户名登录”
# driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
time.sleep(2)

#勾选复选框
driver.find_element_by_xpath('//*[@type="checkbox"]').click()
time.sleep(1)

#取消复选框勾选
driver.find_element_by_xpath('//*[@type="checkbox"]').click()
time.sleep(1)

driver.quit()
