import csv
import codecs
# codecs 是自然语言编码转换模块

fileName = 'PythonBook.csv'

# 指定编码为 utf-8, 避免写 csv 文件出现中文乱码
with codecs.open(fileName, 'w', 'GBK') as csvfile:
    # 指定 csv 文件的头部显示项
    filednames = ['书名', '作者','shabi','fuck']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)

    books = []
    book = {
        'title': '笑傲江湖',
        'author': '金庸',
        "rank":"1",
        "play":"1231346",
    }
    books.append(book)

    writer.writeheader()
    for book in books:
        try:
            writer.writerow({'书名':book['title'], '作者':book['author'],"shabi":book['rank'],'fuck':book['play']})
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
