import requests
from requests.exceptions import RequestException
import re
import  json
def get_one_page(url):
    headers={
        "User-Agent" : "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/58.0.3029.110Safari/537.36SE2.XMetaSr1.0",
    }
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return  None

def parse_one_page(html):
    #print(html)
    pattern=re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?board-item-main">.*?name">.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?score">.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    contents=re.findall(pattern,html)
    #print(contents)
    for content in contents:
        yield {
            "oeder":content[0],
            "name":content[1],
            "stars":content[2].strip()[3:],
            "releasetime":content[3].strip()[5:],
            "score":content[4]+content[5]
        }
        """
        order,name,stars,time,score1,score2=content
        print(order,name,stars,time,score1,score2)
        """
    return contents

def write_into_files(content):
    with open('maoyanTop100.txt','a',encoding='utf-8') as  f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main():
    for offset in range(0,100,10):
        url='http://maoyan.com/board/4?offset='+str(offset)
        html=get_one_page(url)
        #print(html)
        for content in parse_one_page(html):
            write_into_files(content)

if __name__=='__main__':
    main()

