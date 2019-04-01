# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:10:09 2018

@author: admin
"""
'''
def fibo(n):
    f1=1 
    f2=1
    print(f1,'',f2,'', end='')
    for i in range(3,n):
        f3=f2+f1
        print(f3,'',end='')
        f1=f2
        f2=f3
        

fibo(1)
'''
import requests
import pandas
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

response=requests.get('http://haoshu.xshcs.com')
response.encoding='utf-8'
html=response.text
strhtml=BeautifulSoup(html,'lxml')
lists=strhtml.select('[class="title"]')
lists2=strhtml.select('[class="price"]')

df = pandas.DataFrame()
i=0
for fr in lists:
    context = fr.string+ '：'+ lists2[i].string.replace('¥','')
    #print(context)
    i=i+1
    tmp = pandas.DataFrame([context.split('：')], columns=["书名", "价格"])
    df = df.append(tmp, ignore_index=True)


# 加载中文字体
font = fm.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")
# 将价格内容转换为数字类型
df["价格"] = pandas.to_numeric(df["价格"])

# 创建空白图片
fig, ax = plt.subplots()
# 将书名作为x轴，价格作为y轴，创建柱状图
ax.bar(df["书名"], df["价格"], color='green')
# 设置书名作为x轴的记号标签，并垂直显示
ax.set_xticklabels(df["书名"], fontproperties=font, rotation="vertical")

# 设置x y 标签, 并设置中文字体
ax.set_ylabel("价格（元）", fontproperties=font)
ax.set_xlabel("书名", fontproperties=font)

# 设置紧凑布局，防止导出的图片显示不完整
fig.tight_layout()

plt.show()
# plt.savefig("image.jpg")


'''
with open('book.txt','w',encoding='utf-8') as f:
    i=0
    for fr in lists:
        context= fr.string+ '：'+ lists2[i].string.replace('¥','')
        i=i+1
        f.write(context)
'''
        


        


