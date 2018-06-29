from selenium import webdriver

driver = webdriver.Chrome("C:\Users\user.SWZ-RD006\PycharmProjects\untitled1\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.quit()
