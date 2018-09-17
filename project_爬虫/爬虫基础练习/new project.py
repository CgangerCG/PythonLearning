import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pyquery import PyQuery as pq
import json
import time

def one_up_page(url):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    #chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败+
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    driver.get(url)

     #重新加载页面
    def getppage():
        page_content=driver.page_source
        return page_content

    #收集数据
    def search_data():
        content=getppage()
        up=driver.find_element_by_id('h-name')
        name=up.text
        html = pq(content)
        items = html('#submit-video-list .list-list .list-item').items()
        for item in items:
            info = {
                "name":name,
                "aid": item.attr('data-aid'),
                "link": item.find('.c .title-row .title').attr('href')[2:],
                "title": item.find('.c .title-row .title').attr('title'),
                "play": item.find('.c .meta .play').text(),
                "time": item.find('.c .meta .time').text(),
            }
            write_in_file(info)
    def write_in_file(info):
        with open('Count.txt', 'a', encoding='utf-8') as  f:
            f.write(json.dumps(info, ensure_ascii=False) + '\n')
            f.close()
        return
    #跳转下一页
    def next_page():
        button = driver.find_element_by_class_name('be-pager-next')
        ifnext=button.get_attribute('class')
        if ifnext=='be-pager-next':
            button.click()
            return True
        else:
            return False

    search_data()
    while next_page():
        next_page()
        search_data()
    else:
        print('end')
    driver.close()

def more_up_page():
    url='https://space.bilibili.com/{}/#/video?tid=0&page=1&keyword=&order=pubdate'
    for i in range(1,10):
        one_up_page(url.format(str(i)))


if __name__=='__main__':
    more_up_page()