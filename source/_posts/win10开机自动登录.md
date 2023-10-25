---
title: win10开机自动登录
toc: true
---

# win10开机自动登录

1. 开始-运行
2. 输入netplwiz
3. 取消勾选「要使用本计算机，用户必须输入用户名和密码」

# 不显示「要使用本计算机，用户必须输入用户名和密码」的解决办法

1. 开始-运行
2. 输入regedit
3. 找到 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device
4. 双击将2修改为0
5. 重新打开netplwiz就可以了

# 设置开机启动软件

1. 开始-运行
2. 输入shell:startup打开文件夹
3. 将软件快捷方式放入文件夹内

