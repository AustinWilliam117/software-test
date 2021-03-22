from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep,ctime

# 隐式等待和显式等待是可以结合

driver = webdriver.Firefox()

# 隐式等待
driver.implicitly_wait(20)

driver.get("https://cn.bing.com")

try:
    # 显示等待
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,"q")))
    
    driver.find_element_by_xpath('//input[@name="q"]').send_keys("星际穿越")
finally:
    driver.quit()