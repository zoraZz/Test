from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
time.sleep(2)

#方法一，判断单选框是否被选中，推荐
if driver.find_element_by_xpath('//*[@id="newstitle"]').is_selected():
    print('新闻标题被选中')
elif driver.find_element_by_xpath('//*[@id="news"]').is_selected():
    print('新闻全文被选中')
else:
    print('test failed')

#方法二，不管try里面的元素有没有被选中，最后都会打印passed，因为is_selected返回的结果是true/false，布尔值不算异常，所以会正常执行完try后面的语句
# try:
#     driver.find_element_by_xpath('//*[@id="newstitle"]').is_selected()
#     print('test passed')
# except Exception as e:
#     print('test failed',format(e))

driver.quit()