---
title:  选中取消iconfont所有图标
date: {{ date }}
updated: {{ date }}
toc: true
---


打开控制台，粘贴下面代码，回车

```

var ls = document.getElementsByClassName('icon-cover-freeze');
var mClick = function(index) {
    if (index == ls.length) return;
    ls[index].firstElementChild.click();
    setTimeout(() => {
        mClick(index + 1);
    }, 5);
};
mClick(0);

```

