import requests
import lxml.html

# 获取中国天气网天气预报网页
http_response = requests.get("http://www.weather.com.cn/forecast/")
# 设置中文编码
http_response.encoding = "utf-8"

## 将获取的网页HTML保存到4-1.html文件中
#with open("4-1.html", "w", encoding="utf-8") as html:
#    html.write(http_response.text)

html = lxml.html.fromstring(http_response.text)
weather40 = html.xpath('//')