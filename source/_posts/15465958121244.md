---
title:  brew修改为中科大源
date: {{ date }}
updated: {{ date }}
toc: true
---


```shell
$ cd "$(brew --repo)"
$ git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
$ git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-cask"
$ git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile
```
