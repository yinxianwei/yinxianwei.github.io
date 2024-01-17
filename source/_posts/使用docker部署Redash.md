---
title: 使用docker部署Redash
date: 2023-12-13 13:46:35
tags: BI
---

```sh
git clone https://github.com/getredash/redash.git
cd redash/
```

```
# docker-compose.yml同级目录新建文件 .env

REDASH_SECRET_KEY=随机字符串
REDASH_COOKIE_SECRET=随机字符串
GOOGLE_CLIENT_ID=随机字符串
```

```sh
docker-compose up -d
yarn --frozen-lockfile

docker-compose run --rm server create_db

# 测试数据
docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"

open http://localhost:5001/setup
```
