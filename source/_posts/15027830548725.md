---
title:  用Python写爬虫
date: {{ date }}
updated: {{ date }}
toc: true
---



##目标
	
爬取美图天空的图片，并自动下载至本地

##环境

Python3.4+BeautifulSoup

<!-- more -->

##步骤

1. 首先打开[http://www.tootk.net/tupian/bizhi/](http://www.tootk.net/tupian/bizhi/)分析网页内容 ![QQ20150718-2@2x](media/15027830548725/QQ20150718-2@2x.png)

2. `class="w170img"`为每一条内容
3. 里面的`img`内的`src`、`alt`分别为图片链接和名字
4. 有了这两样就可以把图片下载下来了

<!--more-->

##代码

```py
#   语言：Python 3.4

import urllib.request
import bs4,os

page_sum = 10  #设置下载页数

path = os.getcwd()
path = os.path.join(path,'images')
if not os.path.exists(path):
    os.mkdir(path)                                  #创建文件夹
url = "http://www.tootk.net"     #url地址
headers = {                                         #伪装浏览器
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/32.0.1700.76 Safari/537.36'
}

for count in range(page_sum):
    req = urllib.request.Request(
        url = url+"/tupian/bizhi/list_13_"+str(count+1)+".html",
        headers = headers
    )#url拼接
    print(req.full_url)
    content = urllib.request.urlopen(req).read()

    soup = bs4.BeautifulSoup(content,"html5lib")                   # BeautifulSoup 获取网页内容

    liResult = (soup.find_all("div", attrs={"class": "w170img"}))

    for content in liResult:
        image = content.img#遍历img
    
        lplink = image.get('src')#获取图片链接
        title = image.get('alt')#获取图片名称
        link = url+lplink.replace("-lp","")#转换高清图片链接
        filename = path + os.sep + title + ".jpg"#本地存储目录

        print(link)

        urllib.request.urlretrieve(link,filename) #存储
```

参考链接：

- [http://www.cnblogs.com/yupeng/p/3362031.html](http://www.cnblogs.com/yupeng/p/3362031.html)
- [http://www.jianshu.com/p/b87413a9307e](http://www.jianshu.com/p/b87413a9307e)
- [http://wuchong.me/blog/2014/01/27/python-spider-gif/](http://wuchong.me/blog/2014/01/27/python-spider-gif/) 

