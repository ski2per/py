import requests
import lxml.html

# 获取网易云阅读文字作品网页
http_response = requests.get("http://yuedu.163.com/book/category/category/2100")
# 设置中文编码
http_response.encoding = "utf-8"

# 将HTTP响应的HTML文本通过lxml.html.fromstring方法
# 转换成可以使用XPath的来分析的对象
html = lxml.html.fromstring(http_response.text)

# 通过网页左侧书籍所在的div元素的class属性来获取所有左侧的所有书籍
left_books = html.xpath('//div[@class="yd-book-item yd-book-item-pull-left"]')
# 通过网页右侧书籍所在的div元素的class属性来获取所有右侧的所有书籍
right_books = html.xpath('//div[@class=yd-book-item yd-book-item-pull-left edge-right"]')

# 将两个书籍列表合并，得到本页所有书籍
books = left_books + right_books

# 通过python的循环来依次获取我们所需要的书籍信息
for book in books:
    # 获取标题
    title = book.xpath('.//h2')[0].text_content()
    # 获取作者
    author = book.xpath('.//dd')[0].text_content()
    # 获取评分
    spans = book.xpath('.//span[@class="no"]')
    rate = 5 - len(spans)

    # 格式化输出
    print('<<{}>>, 作者: {}, 评分: {}'.format(title, author, rate))

