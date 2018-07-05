from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://tieba.baidu.com/index.html')
driver.maximize_window()
time.sleep(2)

#执行JS脚本，触发一个alert弹窗
driver.execute_script("window.alert('这是弹窗');")
time.sleep(2)

#点击“确定”，关闭弹窗，方法一：
# driver.switch_to_alert().accept()
#方法二，注意alert后面没有括号：
driver.switch_to.alert
time.sleep(2)

#执行JS脚本，控制浏览器竖向滚动条
# target_ele = driver.find_element_by_link_text('地区')
# driver.execute_script("return arguments[0].scrollIntoView();",target_ele)

driver.quit()