import requests
from bs4 import  BeautifulSoup

r = requests.get("https://space.bilibili.com/11722013/#/video")
print(r.status_code)
r.encoding="utf-8"
#print(r.text)
soup = BeautifulSoup(r.text)
print(soup.find_all("title"))
print(soup.find_all('span'))
import re
print(soup.find_all(string=re.compile('科技')))
