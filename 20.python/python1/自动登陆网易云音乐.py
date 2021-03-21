from selenium import webdriver
from time import sleep
# 创建一个火狐浏览器对象
webdriver = webdriver.Firefox()
# 获取URL
webdriver.get('https://music.163.com/')
# 等待2秒
sleep(2)
# 找到登录按钮，并点击
webdriver.find_element_by_xpath('//a[@data-action="login"]').click()
# 找到其他方式登录按钮，并点击
webdriver.find_element_by_xpath('//a[@data-action="switch"]').click()
# 点击许可用户协议
webdriver.find_element_by_xpath('//input[@id="j-official-terms"]').click()
# 点击手机登录
webdriver.find_element_by_xpath('//a[@data-type="mobile"]').click()
# 用户名输入手机号
webdriver.find_element_by_xpath('//input[@id="p"]').send_keys('17610832710')
# 密码输入123456
webdriver.find_element_by_xpath('//input[@id="pw"]').send_keys('123456')
# 等待10秒
sleep(10)
# 释放进程
webdriver.quit()