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
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
time.sleep(2)

#到登录窗口点击“登录”按钮
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
time.sleep(2)

#判断错误信息
error_message = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__error"]').text

try:
    assert error_message == '请您输入手机/邮箱/用户名'
    print('test passed')
except Exception as e:
    print('test failed',format(e))

driver.quit()