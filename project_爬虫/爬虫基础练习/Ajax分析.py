import requests
import json
headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
    }
url='https://space.bilibili.com/8969156/#/video'
link='https://space.bilibili.com/ajax/member/GetInfo'
gesinfo=requests.get(url,headers=headers)
print(gesinfo.text,gesinfo)
