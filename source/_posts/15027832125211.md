---
title:  Swift方法声明可选参数
date: {{ date }}
updated: {{ date }}
toc: true
---



声明

```swift
str2:String? = nil
```

如：

```swift
func test(str:String, str2:String? = nil){
}
test("哈哈");
test("哈哈", str2: "哈哈哈");
```

