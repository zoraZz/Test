from selenium import webdriver
import time

# 时间格式进行格式化
current_time = time.strftime('%Y_%m_%d_%H_%M_%S')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

#获取百度首页截图，并保存
#第一种方法：
# capturename = '截图' + current_time
# driver.get_screenshot_as_file('C:\\Users\\user.SWZ-RD006\\Desktop\\%s.png'%capturename)

#第二种方法：
driver.get_screenshot_as_file('C:\\Users\\user.SWZ-RD006\\Desktop\\截图' + current_time + '.png')

#区域截图:截取全屏图片并保存 -> 获取元素位置、大小 -> 截取元素图片并保存



driver.quit()