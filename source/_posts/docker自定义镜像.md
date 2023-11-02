---
title: docker自定义镜像
date: 2023-11-02 15:36:52
tags: docker
toc: true
---

# 环境

```sh
MacOS Ventura 13.5.2
Docker v4.24.2
```

# 基于ubuntu镜像添加自动服务

```sh
docker pull ubuntu:20.04
```

```sh
# 运行镜像
docker run -it ubuntu:20.04 /bin/bash
# 备份源
mv /etc/apt/sources.list /etc/apt/sources.list.back

# 修改源

echo  "# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# # deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse" > /etc/apt/sources.list

apt update

# 安装nginx

apt install nginx
```

# 创建自定义镜像

```sh
# 查看container_id
docker ps -a

docker commit container_id new_image_name:new_tag

# container_id 是要打包的容器的 ID 或名称。
# new_image_name 是你为新镜像指定的名称。
# new_tag 是新镜像的标签。

# 比如：
docker commit 9252c4f9d3ce my_image:1.0

# 查看镜像
docker images
```

# 运行自定镜像并指定端映射

```sh
# 将容器内的 HTTP 服务器的端口 80 映射到主机的端口 8080
docker run -p 8080:80 -it my_image:1.0 /bin/bash

# 执行
nginx

# 访问本地http://localhost:8080
```

# 镜像打包

```sh
docker save -o my_image.tar my_image:1.0
```

# 其它docker命令

```sh
# 访问容器
docker exec -it <CONTAINER ID> /bin/bash

# 拷贝容器文件至本地
docker cp <IMAGE>:<容器路径> <本地路径>

# 拷贝本地文件至容器
docker cp <本地文件> <IMAGE>:<容器路径>
```
