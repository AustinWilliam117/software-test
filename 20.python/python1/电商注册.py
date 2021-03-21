from selenium import webdriver
from time import sleep
# 创建一个浏览器对象
webdriver = webdriver.Firefox()
# 访问指定URL
webdriver.get('http://192.168.1.100/shopxo/index.php')
# 等待一秒
sleep(1)
# 寻在注册按钮，点击注册
webdriver.find_element_by_xpath('//a[text()="注册"]').click()
# 在用户名栏输入666666
webdriver.find_element_by_xpath('//input[@name="accounts"]').send_keys('666666')
# 在密码栏输入111111
webdriver.find_element_by_xpath('//input[@name="pwd"]').send_keys('111111')
# 勾选阅读并同意 《服务协议》
webdriver.find_element_by_xpath('//label[@class="am-checkbox am-success c-p"]').click()
# 释放进程
webdriver.quit()