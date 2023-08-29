---
title:  Jenkins
date: {{ date }}
updated: {{ date }}
toc: true
---



API: https://www.jenkins.io/doc/pipeline/steps/workflow-multibranch/

语法： groovy


示例

```
node() {
    // 步骤
    stage('build') {
        dir('切换目录') {
            // env.BRANCH_NAME 分支名
            // 拉取分支
            git branch: env.BRANCH_NAME, url: 'git@xxxx.git'
            // 配置
            properties([
                // 不允许并发构建
                disableConcurrentBuilds(),
                // 丢弃旧的构建
                buildDiscarder(logRotator(daysToKeepStr: '3', numToKeepStr: '5')),
                // 参数化构建过程
                parameters([
                    // 字符串
                    string(name: 'VERSION', defaultValue: '1.0.0', description: '请输入版本号'),
                    // 选项
                    choice(name: 'TYPE', choices: ['1', '2', '3'], description: '选择类型')
                ]),
                // 轮询SCM
                pipelineTriggers([
                    pollSCM('H/10 * * * *')
                ])
            ])
            // 执行命令
            sh('yarn build')
        }
    }
}
```