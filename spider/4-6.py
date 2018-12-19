import requests
import lxml.html


for page in range(1, 10):
    url = 'http://yuedu.163.com/book/category/category/2100/0_0_1/p{}/s20'.format(page)

    # 获取网易云阅读文字作品网页
    http_response = requests.get(url)
    # 设置中文编码
    http_response.encoding = "utf-8"

    html = lxml.html.fromstring(http_response.text)

    # 通过谷歌开发者工具来辅助获取书籍列表的<div>元素
    books = html.xpath('//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div')

    print("====== 第{}页, 书籍{}本 ======".format(page, len(books)))

    for book in books:
        title = book.xpath('.//h2')[0].text_content()
        author = book.xpath('.//dd')[0].text_content()

        print('<<{}>>, 作者: {}'.format(title, author))

