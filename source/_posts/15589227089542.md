---
title:  微信JS分享iOS不回调success方法
date: {{ date }}
updated: {{ date }}
toc: true
---


添加一个`setTimeout`就好了

```
...
success: function(results) {
    setTimeout(function() {
        // some
    }, 500);
}
```