from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
time.sleep(2)

#并未实现新开标签页
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
time.sleep(2)
newTab = driver.title
print('当前title：',newTab)
if (newTab == '新标签页'):
    print('test passed')
else:
    print('test failed')

# driver.quit()