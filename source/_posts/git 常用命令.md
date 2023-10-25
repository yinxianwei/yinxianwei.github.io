---
title:  git 常用命令
date: {{ date }}
updated: {{ date }}
toc: true
---


## 常用
###### 拉取

```
git pull
```

###### 提交

```
git add .
git add <file_path...>
git add -p
```

<!-- more -->

###### 暂存

```
git commit -m "commit message"
```
###### 推送

```
git push
```
###### 遴选

```
git cherry-pick <commit id>
```

###### 重置提交

```
# 重置所有修改
git checkout .
# 所有未提交内容暂存至stash，可用git stash pop恢复
git stash
# 重置到某个节点，保留修改
git reset --soft HASH
# 重置到某个节点，舍弃修改
git reset --hard HASH
```

###### 变更查看

```
# 查看没有add的修改
git diff
# 查看已经add的修改
git diff --cached
# 所有修改
git diff HEAD
```

## 标签

###### 标签列表

```
git tag
git tag -l 'v1.*'
```
[glob pattern](https://en.wikipedia.org/wiki/Glob_(programming))

###### 标签列表格式化

```
git tag -l --format='%(refname:short) %(taggerdate)'
```
[ git-for-each-ref[1] ](https://git-scm.com/docs/git-for-each-ref)

###### 新建标签

```
git tag v1.0.0
```

###### 推送标签

```
git push origin v1.0.0
```
######推送全部标签

```
git push origin --tags
```

###### 删除本地标签

```
git tag -d v1.0.0
```

###### 批量删除本地标签
```
git tag | grep "v1.*" |xargs git tag -d
```

###### 删除远程标签

```
git push origin :refs/tags/v1.0.0
```

## 分支

###### 新建分支

```
git branch dev
```

###### 切换分支

```
git checkout dev
```

###### 新建并切换

```
git checkout -b dev
```

###### 删除分支

git branch -d dev

###### 合并分支

```
git merge dev
```

## 自定义快捷命令

```
.gitconfig

[alias]
st = status
co = checkout
br = branch
mg = merge
ci = commit
md = commit –amend
dt = difftool
mt = mergetool
last = log -1 HEAD
cf = config
line = log –oneline
latest = for-each-ref –sort=-committerdate –format=’%(committerdate:short) %(refname:short) [%(committername)]’
```

