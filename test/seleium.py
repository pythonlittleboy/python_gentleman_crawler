from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

driver = webdriver.Chrome()
driver.get('http://www.clpig.org/torrent/MDB-740.html')

#assert "磁力猪 | 磁力搜索_番号搜索_BT搜索_种子搜索 - 磁力链接搜索引擎" in driver.title

elem = driver.find_element_by_id("input")
elem.send_keys("ABP-572")
elem.send_keys(Keys.RETURN)

time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[1])

print(driver.page_source)

driver.quit()