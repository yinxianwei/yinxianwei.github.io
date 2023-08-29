---
title:  testlink macos12
date: {{ date }}
updated: {{ date }}
toc: true
---



brew install php7.4

`.zshrc`

```
export PATH="/usr/local/opt/php@7.4/bin:$PATH"
export PATH="/usr/local/opt/php@7.4/sbin:$PATH"
export LDFLAGS="-L/usr/local/opt/php@7.4/lib"
export CPPFLAGS="-I/usr/local/opt/php@7.4/include"
```

后台启动
  brew services start php@7.4
  
  直接启动

  /usr/local/opt/php@7.4/sbin/php-fpm --nodaemonize
  
  
  创建证书
  
  https://www.simplified.guide/macos/keychain-cert-code-signing-create
  
  签名
  
   codesign -s "YOUR CERTIFICATE NAME" --keychain ~/Library/Keychains/login.keychain-db /usr/local/opt/php@7.4/lib/httpd/modules/libphp7.so

  
  修改httpd配置
  `/private/etc/apache2/httpd.conf`
  添加
  `LoadModule php7_module /usr/local/opt/php@7.4/lib/httpd/modules/libphp7.so "YOUR CERTIFICATE NAME"`

文件末尾添加

```
<FilesMatch \.php$>
    SetHandler application/x-httpd-php
</FilesMatch>
```


启动服务
sudo apachectl start



https://www.cnblogs.com/qinjuan/articles/13917203.html