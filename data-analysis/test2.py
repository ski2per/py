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


font = fm.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")
df["价格"] = pandas.to_numeric(df["价格"])

fig, ax = plt.subplots()
ax.bar(df["书名"], df["价格"], color='green')
ax.set_xticklabels(df["书名"], fontproperties=font, rotation="vertical")
ax.set_ylabel("价格（元）", fontproperties=font)
ax.set_xlabel("书名", fontproperties=font)
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
        


        


