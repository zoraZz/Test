from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

#先定位到需要右击的图片位置
element = driver.find_element_by_xpath('//*[@id="lg"]/img[1]')
#Context_click:右键，ARROW_DOWN：通过键盘向下箭头来选择菜单，perform：执行
ActionChains(driver).context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()


