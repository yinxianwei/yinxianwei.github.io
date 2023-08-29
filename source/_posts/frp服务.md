---
title: frp服务
date: 2023年05月12日10:55:01
toc: true
---

# 服务端配置

- 查看服务器架构

```sh
dpkg --print-architecture
```

- 下载

```
# 下载  https://github.com/fatedier/frp/releases
wget https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz
tar -xf frp_0.48.0_linux_amd64.tar.gz
cd frp_0.48.0_linux_amd64
```

- 配置

```ini
# frps.ini
# 文档地址 https://gofrp.org/docs/reference/server-configures/

[common]
bind_addr = 0.0.0.0
bind_port = 7000
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = admin

vhost_http_port = 8080
vhost_https_port = 4443
token = xxxx
subdomain_host = yourdomain2.com
```

- 开机启动

```sh
# /etc/systemd/system/frps.service

[Unit]
# 服务名称，可自定义
Description = frp server
After = network.target syslog.target
Wants = network.target

[Service]
Type = simple
# 启动frps的命令，需修改为您的frps的安装路径
ExecStart = /root/app/frp_0.48.0_linux_amd64/frps -c /root/app/frp_0.48.0_linux_amd64/frps.ini

[Install]
WantedBy = multi-user.target


```

- 命令

```sh

# 启动frp
systemctl start frps
# 停止frp
systemctl stop frps
# 重启frp
systemctl restart frps
# 查看frp状态
systemctl status frps

#开机启动
systemctl enable frps
```


# 客户端配置（Mac intel）

- 下载

```sh

https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_darwin_amd64.tar.gz

```
- 配置

```ini
# frpc.ini

[common]
server_addr = x.x.x.x
server_port = 7000
token = xxxx

[web2]
type = http
local_port = 8080
custom_domains = www

```
- 启动

```sh
./frpc -c ./frpc.ini
```

# nginx配置


```sh
# /etc/nginx/conf.d/www.conf
server {
    listen 80;
    server_name www.yourdomain2.com;
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_redirect http://$host/ http://$http_host/;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
    }
}
```
