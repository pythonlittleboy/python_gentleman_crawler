from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

driver = webdriver.Chrome()
driver.get('http://www.ciliba.org/s/MDB-740.html')
time.sleep(3)
driver.execute("confirm")
print(driver.page_source)
driver.close()
driver.quit()