from selenium import webdriver
from time import sleep

webdriver = webdriver.Chrome()
# 隐式等待
webdriver.implicitly_wait(10)

webdriver.get('https://www.baidu.com/')

webdriver.find_element_by_id('kw').send_keys('虚竹')

webdriver.find_element_by_id('su').click()

sleep(1)

webdriver.find_element_by_xpath('//em[text()="虚竹"]/..').click()

# 获取handles
handles = webdriver.window_handles
# print(handles)

# 关闭当前handles
webdriver.close()

# 切换handles
webdriver.switch_to.window(handles[1])

sleep(5)

webdriver.find_element_by_xpath('//a[text()="天龙八部"]').click()

