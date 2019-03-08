import requests
import lxml.html

# 获取网易云阅读文字作品网页
http_response = requests.get("http://yuedu.163.com/book/category/category/2100")
# 设置中文编码
http_response.encoding = "utf-8"

# 将HTTP响应的HTML文本通过lxml.html.fromstring方法
# 转换成可以使用XPath的来分析的对象
html = lxml.html.fromstring(http_response.text)

# 通过谷歌开发者工具来辅助获取书籍列表的<div>元素
books = html.xpath('//*[@id="page-163-com"]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div')

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

