from selenium import webdriver
url='https://space.bilibili.com/11722013/#/video'
driver=webdriver.Chrome()
driver.get(url)
print(driver.page_source)
