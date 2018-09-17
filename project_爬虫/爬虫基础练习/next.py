from selenium import webdriver
import time
url='https://space.bilibili.com/9321359/#/video?tid=0&page=2&keyword=&order=pubdate'
driver=webdriver.Chrome()
driver.get(url)
button = driver.find_element_by_class_name('be-pager-next')
button.click()
content=driver.page_source
print(content)
driver.close()