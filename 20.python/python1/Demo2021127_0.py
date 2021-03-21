from selenium import webdriver
from time import sleep

# 定义一个chrome浏览器驱动，用于后续的浏览器相关操作
webdriver = webdriver.Chrome()
# 通过get方法实现了浏览器的调用，以及URL的访问
webdriver.get('https://www.baidu.com')
# 通过name属性来查找特定的元素,输入虚竹
webdriver.find_element_by_name('wd').send_keys('python')
# 通过id属性查找特定的元素，点击操作
webdriver.find_element_by_id('su').click()
# 等待10秒，等待百度搜索完毕
sleep(5)
# 点击第一条查询结果
webdriver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# 释放资源
sleep(5)
webdriver.quit()
