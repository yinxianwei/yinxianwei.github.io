---
title:  Mac修改屏幕快照保存的位置
date: {{ date }}
updated: {{ date }}
toc: true
---


```
$ defaults write com.apple.screencapture location <path>
$ killall SystemUIServer
```