---
title:  vue-cli3.0.1 多页面超过5个后无法打包
date: {{ date }}
updated: {{ date }}
toc: true
---


```js
// vue.config.js

module.exports = {
  // ...
  chainWebpack: config => config.plugins.delete('named-chunks')
}

```

详情见： [https://github.com/vuejs/vue-cli/issues/1996#issuecomment-415022624](https://github.com/vuejs/vue-cli/issues/1996#issuecomment-415022624)