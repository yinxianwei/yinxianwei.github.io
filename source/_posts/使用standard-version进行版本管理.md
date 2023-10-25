---
title:  使用standard-version进行版本管理
date: {{ date }}
updated: {{ date }}
toc: true
---





    "standard-version": {
        "issueUrlFormat": "http://redmine.mei1.info/issues/{{id}}",
        "commitUrlFormat": "http://git.mei1.info/yinxianwei/test-version/commit/{{hash}}"
    }



        "commitUrlFormat": "http://git.mei1.info/yinxianwei/test-version/commit/{{hash}}"

 
 
 yarn run release
 git push --follow-tags origin test
 git checkout master && git pull && git merge test && git push
 git checkout hotfix && git pull && git merge test && git push



        git push --set-upstream origin hotfix