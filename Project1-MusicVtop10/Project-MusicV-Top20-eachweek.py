#此项目爬取音乐V榜内地专辑销量周榜
import requests
import re
from requests.exceptions import RequestException
import json
from pyquery import PyQuery as pq
import codecs
import csv
def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    content = response.text
    try:
        if response.status_code == 200:
            print(200)
    except RequestException:
        print('ERROR')
    doc = pq(content)
    # print(doc('.v_date_con .J_toggle_date_picker').text())
    items = doc('#rankList .vitem').items()
    for item in items:
        field = {
            "name": item.find('.mv_info .info .album-title .title').text(),
            "type": '专辑',
            "rank": 11- int(item.find('.top_num').text()),
            "time": doc('.v_date_con .J_toggle_date_picker').text()[:10],
        }
        write_in_file(field)

def write_in_file(info):
    with open('Project-MusicV-Top20-eachweek.csv', 'a', encoding='GBK') as f :
        headers=['name', 'type', 'rank', 'time']
        writer = csv.DictWriter(f, headers)
        books = []
        books.append(info)
        for book in books:
            try:
                writer.writerow(
                    {'name': book['name'], 'type': book['type'], "rank": book['rank'], 'time': book['time']})
            except UnicodeEncodeError:
                print("编码错误, 该数据无法写到文件中, 直接忽略该数据")


def get_more_pages():
    url='http://vchart.yinyuetai.com/album/weekly?type=ml&period={}'
    for i in range(1,128):
        get_one_page(url.format(str(i)))

if __name__ == '__main__':
    get_more_pages()

