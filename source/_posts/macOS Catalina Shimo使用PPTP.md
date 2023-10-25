---
title:  macOS Catalina Shimo使用PPTP
date: {{ date }}
updated: {{ date }}
toc: true
---


##### 环境：
    macOS Catalina 10.15.3
    Shimo 4.1.5.1

##### 下载文件

[下载pptp和PPTP.ppp](https://zhuanlan.zhihu.com/p/107789298) 链接: https://pan.baidu.com/s/1lANcpclyTMJPZZLcgOpXFQ 提取码: vbr9

下载[VPN Tracker 365](https://www.vpntracker.com/)

##### 使用方法

1. [关闭系统SIP](https://www.jianshu.com/p/69fb68577dc8)
2. 复制`PPTP.ppp`文件至`/系统/资源库/Extensions/`
3. 打开VPN Tracker 365，试用，添加PPTP，连接时会自动下载PPTP组件（需登录）
4. 使用VPN Tracker 365连接成功后打开Shimo.app再连接PPTP就可以了
