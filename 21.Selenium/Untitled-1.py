from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://cn.bing.com")

# 获取当前窗口
handle = driver.current_window_handle

driver.find_element_by_xpath('//input[@name="q"]').send_keys("星际穿越")
driver.find_element_by_xpath('//input[@name="go"]').click()

sleep(2)

# 使用JS打开新标签
js = 'window.open("https://www.baidu.com");'
driver.execute_script(js)

# 获取所有窗口
handles = driver.window_handles
# 关闭当前窗口
driver.close()
# 切换窗口
driver.switch_to.window(handles[1])

sleep(2)

driver.find_element_by_name("wd").send_keys("星际穿越")

sleep(2)
driver.quit()