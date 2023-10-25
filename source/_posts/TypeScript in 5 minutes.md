---
title:  TypeScript in 5 minutes
date: {{ date }}
updated: {{ date }}
toc: true
---



## 类型注解

```js
// js

function greeter(person) {
}

// ts

function greeter(person: string) {
}
```

## 接口

```js
interface Person{
    firstName: string,
    lastName: string
}

function greeter(person: Person) {
}

let user = {
    firstName: 'J',
    lastName: 'N'
};
// 内部结构兼容则兼容
greeter(user);
```

## 类

```ts

// 使用public可以自动创建该名称的属性
class Student {
    fullName: String,
    constructor(public firstName: string, public lastName: string) {
        this.fullName = firstName+lastName;
    }
}
let user = new Student('J', 'N');

```
