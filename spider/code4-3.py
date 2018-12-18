import requests
import lxml.html

# 获取网易云阅读文字作品网页
http_response = requests.get("http://yuedu.163.com/book/category/category/2100")
# 设置中文编码
http_response.encoding = "utf-8"

html = lxml.html.fromstring(http_response.text)

# 通过谷歌开发者工具获取书籍列表的div元素的XPath
# book_list_div = html.xpath('//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]')[0]
left_books = html.xpath('//div[@class="yd-book-item yd-book-item-pull-left"]')

right_books = html.xpath('//div[@class="yd-book-item yd-book-item-pull-left edge-right"]')

books = left_books + right_books

for book in books:
    title = book.xpath('.//h2')[0].text_content()
    author = book.xpath('.//dd')[0].text_content()
    spans = book.xpath('.//span[@class="no"]')
    rate = 5 - len(spans)

    print('<<{}>>, 作者: {}, 评分: {}'.format(title, author, rate))

