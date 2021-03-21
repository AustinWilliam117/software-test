# from selenium import webdriver
#
# fireFoxOptions = webdriver.FirefoxOptions()
#
# fireFoxOptions.set_headless()
#
# brower = webdriver.Firefox()
#
# # brower.get('http://www.baidu.com')
# brower.get('http://192.168.1.101/shopxo/index.php')
#
# # print(brower.page_source)
#
# # brower.close()


from selenium import webdriver
from time import sleep

webdriver = webdriver.Firefox()

webdriver.get('https://www.douban.com/')

webdriver.find_element_by_name('q').send_keys('星际穿越')
webdriver.find_element_by_class_name('nb').click()

