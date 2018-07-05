from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a').click()
#输出当前窗口句柄
print(driver.current_window_handle,driver.title)
#获取当前全部窗口句柄集合
handels = driver.window_handles
#输出句柄集合
print(handels)

#切换窗口
for handel in handels:
    if handel != driver.current_window_handle:
        print('switch to second window',handel)
        #关闭第一个窗口
        driver.close()
        #切换到第二个窗口
        driver.switch_to.window(handel)








