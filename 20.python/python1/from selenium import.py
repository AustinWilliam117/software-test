from selenium import webdriver
from time import sleep

webdriver = webdriver.Firefox()

webdriver.get('http://101.133.169.100/yuns/index.php')

# webdriver.find_element_by_name("q").send_keys('星际穿越')
webdriver.find_element_by_link_text("登录").click()

webdriver.find_element_by_name("username").send_keys("1234567")
webdriver.find_element_by_name("password").send_keys("123456")

webdriver.find_element_by_partial_link_text("忘记").click()
sleep(2)

webdriver.find_element_by_class_name("input1").send_keys("123")
webdriver.find_element_by_class_name("input2").send_keys("456")


# 等待10秒
sleep(10)
# 释放进程
webdriver.quit()