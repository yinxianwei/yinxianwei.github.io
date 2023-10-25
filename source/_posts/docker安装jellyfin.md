---
title: docker安装jellyfin
date: 2023-10-24 15:24:07
tags:
---

```
docker pull jellyfin/jellyfin
```

```
docker run -d \
 -p 8096:8096 \
 --name jellyfin \
 --volume /volume2/docker/jellyfin/config:/config \
 --volume /volume2/docker/jellyfin/cache:/cache \
 --mount type=bind,source=/volume2/video,target=/video \
 --restart=unless-stopped \
 jellyfin/jellyfin
```

open [http://localhost:8096/web/index.html](http://localhost:8096/web/index.html)

