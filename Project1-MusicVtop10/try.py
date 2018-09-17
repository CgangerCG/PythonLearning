import requests
import re
import json
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
url='http://vchart.yinyuetai.com/album/weekly?type=ml&period=127'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}
response = requests.get(url, headers=headers)
content=response.text
try:
    if response.status_code == 200:
        print(200)
except RequestException:
    print('ERROR')
doc=pq(content)
#print(doc('.v_date_con .J_toggle_date_picker').text())
items=doc('#rankList .vitem').items()
for item in items:
    field={
        "time":doc('.v_date_con .J_toggle_date_picker').text(),
        "name":item.find('.album-title .title').text(),
        "rank":item.find('.top_num').text(),

    }
    print(field)
