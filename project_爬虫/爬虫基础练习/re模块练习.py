import requests
import re
import time
response= requests.get('https://book.douban.com/').text
#print(response)

pattern=re.compile('<li.*?class="info">.*?class="title".*?title="(.*?)">.*?class="author">(.*?)</div>.*?class="year">(.*?)</span>.*?class="publisher">(.*?)</span>.*?</li>',re.S)
results=re.findall(pattern,response)
#print(results)
for result in results:
    url,name,author,year=result
    name=re.sub('\s','',name)
    author=re.sub('\s','',author)
    year=re.sub('\s','',year)
    print(url,name,author,year)


#'<dd>.*?movie-item-info">.*?title="(.*?).*?star">.*?(.*?)</p>.*?releasetime">(.*?)</P>".*?</dd>',