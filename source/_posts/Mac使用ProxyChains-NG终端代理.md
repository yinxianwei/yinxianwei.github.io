---
title:  Mac使用ProxyChains-NG终端代理
date: {{ date }}
updated: {{ date }}
toc: true
---


安装

`brew install proxychains-ng`

配置

`/usr/local/etc/proxychains.conf`

```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
http 127.0.0.1 1087
socks5 	127.0.0.1 1086
```


可选

`brew install git`

```
// .bash_profile
export PATH=/usr/local/bin:/usr/local/bin:${PATH}
```


`source ~/.bash_profile`

查看代理结果

`proxychains4 curl cip.cc`
