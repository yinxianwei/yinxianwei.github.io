---
title:  GitBook的安装和使用
date: {{ date }}
updated: {{ date }}
toc: true
---



##GitBook官网

[https://github.com/GitbookIO/gitbook](https://github.com/GitbookIO/gitbook)

##Node.js安装
[Nodejs官网](http://nodejs.org/download/)下载`pkg`安装文件，一键安装
##Gitbook安装		
###终端命令：

$ npm install gitbook -g

###dmg编辑器下载连接		
[https://github.com/GitbookIO/editor/releases](https://github.com/GitbookIO/editor/releases)

##编写图书
![QQ20150212-1](media/15027829805094/QQ20150212-1.png)


<!-- more -->

##图书输出
###静态网页

$ gitbook build ./图书目录 --output=./输出目录

###PDF	
需要安装：[gitbook-pdf](https://github.com/GitbookIO/gitbook-pdf)		
npm方式安装`失败`可去官网[http://phantomjs.org/](http://phantomjs.org/)下载安装。

终端命令：

$ gitbook pdf ./图书目录

###eBook
需安装：[ebook-convert](http://manual.calibre-ebook.com/cli/ebook-convert.html)

终端命令：

$ gitbook epub ./图书目录


参考:		
[http://gitbook-zh.wanqingwong.com/howtouse/gitbookcli.html](http://gitbook-zh.wanqingwong.com/howtouse/gitbookcli.html)

[http://www.linuxeden.com/html/softuse/20140409/150458.html](http://www.linuxeden.com/html/softuse/20140409/150458.html)


