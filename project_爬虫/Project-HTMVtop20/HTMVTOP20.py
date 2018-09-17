#此项目爬取HTMVTop20
import requests
import re
from requests.exceptions import RequestException
import json
from pyquery import PyQuery as pq
import codecs
import csv
import datetime
import time
def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.get(url,timeout=1000)
    content = response.text
    try:
        if response.status_code == 200:
            print(200)
    except RequestException:
        print('ERROR')
    doc = pq(content)
    # print(doc('.v_date_con .J_toggle_date_picker').text())
    items = doc('.search-rank .search-rank_L #rankList .vitem').items()
    for item in items:
        field = {
            "name": item.find('.mv_info .info .mvname').text(),
            "type": item.find('.mv_info .info .cc .special').text(),
            "rank": item.find('.score_box .desc-score').text(),
            "time": doc('.v_date_con .J_toggle_date_picker').text()[:9],
        }
        write_in_file(field)

def write_in_file(info):
    with open('HTMVTop20.csv', 'a', encoding='GBK') as f :
        headers=['name', 'type', 'rank', 'time']
        writer = csv.DictWriter(f, headers)
        books = []
        books.append(info)
        for book in books:
            try:
                writer.writerow({'name': book['name'], 'type': book['type'], "rank": book['rank'], 'time': book['time']})
            except UnicodeEncodeError:
                print("编码错误, 该数据无法写到文件中, 直接忽略该数据")


def get_more_pages():
    url='http://vchart.yinyuetai.com/vchart/v?area=HT&date={}'
    d1 = datetime.datetime.strptime('20180820', '%Y%m%d')
    d2 = datetime.datetime.strptime('20180903', '%Y%m%d')
    delta = datetime.timedelta(days=7)
    while d1<=d2:
        i=d1.strftime('%Y%m%d')
        get_one_page(url.format(i))
        d1=d1+delta
        print(d1)
    #get_one_page(url)
if __name__ == '__main__':
    get_more_pages()