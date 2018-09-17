import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import lxml
import time
from pyquery import PyQuery as pq

"""
headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/58.0.3029.110Safari/537.36SE2.XMetaSr1.0",
}
"""

def page_one_search():
    url = "https://space.bilibili.com/8969156/#/video?tid=0&page=1&keyword=&order=pubdate"
    driver=webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    def next_page():
        button = driver.find_element_by_class_name('be-pager-next')
        button.click()
        return
    i=0
    while i<10:
        i=i+1

        content=driver.page_source
    #使用pyquery解析
        html=pq(content)
        items=html('#submit-video-list .list-list .list-item').items()
        for item in items:
            info={
                "aid":item.attr('data-aid'),
                "link":item.find('.c .title-row .title').attr('href')[2:],
                "title":item.find('.c .title-row .title').attr('title'),
                "play":item.find('.c .meta .play').text(),
                "time":item.find('.c .meta .time').text(),
             }
        print(info)
        time.sleep(10)
        next_page()
        time.sleep(10)
    driver.quit()

def main():
   page_one_search()

if __name__== '__main__':
    main()