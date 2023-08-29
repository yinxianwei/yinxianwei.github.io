---
title:  Catalina 10.15.4无法使用SSH域名登录
date: {{ date }}
updated: {{ date }}
toc: true
---




https://tyler.io/so-uh-i-think-catalina-10154-broke-ssh/

方案一

.ssh/config文件添加 `ProxyCommand nc %h %p`

如：

```
host vps
hostname xx.xxx.com
user root
ProxyCommand nc %h %p
```

方案二


`brew install openssh`

~/.bash_profile 添加: export PATH="/usr/local/sbin:$PATH"

`source ~/.bash_profile`
