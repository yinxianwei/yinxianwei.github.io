---
title:  Odoo10 macOS开发环境配置
date: {{ date }}
updated: {{ date }}
toc: true
---


1. 执行 `xcode-select --install` ，如果已安装请忽略
2. 下载odoo10，执行 `git clone https://www.github.com/odoo/odoo --depth 1 --branch 10.0 --single-branch odoo10`
    1. 速度慢使用镜像： `git clone https://gitee.com/mirrors/odoo.git --depth 1 --branch 10.0 --single-branch odoo10`
3. 安装[Python2](https://www.python.org/downloads/)
4. 安装[pip](https://pip.pypa.io/en/stable/installation/)
    1. `curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py`
    2. `python get-pip.py`
    3. 需要在`.bash_profile`或`.zprofile`添加`export PATH=~/Library/Python/2.7/bin:${PATH}`
    4. pip镜像使用，执行`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
       1. 镜像说明： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
        <!-- more -->
5. `cd odoo10`
6. 注释requirements.txt的 `Pillow==3.4.1` `python-ldap==2.4.27` `reportlab==3.3.0`
7. `pip install -r requirements.txt`
    1. pip install python-ldap==2.4.27 --global-option=build_ext --global-option="-I$(xcrun --show-sdk-path)/usr/include/sasl"
    2. pip install reportlab
    3. pip install Pillow==4.0.0
8. 安装[postgresapp](https://postgresapp.com/downloads_legacy.html)，[点击直接下载](https://github.com/PostgresApp/PostgresApp/releases/download/v2.4.4/Postgres-2.4.4-9.5-9.6-10-11-12-13.dmg)
    1. 点击`initialize`初始化
9. 安装node https://nodejs.org/en/
    1. 执行`sudo npm install -g less@3.0.4 less-plugin-clean-css`
10. 启动Odoo
    1. `python odoo-bin --addons-path=addons --db-filter=postgres `
    2. [配置说明](https://www.odoo.com/documentation/10.0/reference/cmdline.html#reference-cmdline)
    3. 打开 [http://localhost:8069/](http://localhost:8069/)
    4. 创建数据库
    5. 执行`python odoo-bin --addons-path=addons --db-filter=数据库名字`
11. vscode启动odoo10配置调试
    插件： 
    1. Pylance
    2. Python `v2022.2.1924087327` 注意版本
    
    .vscode/launch.json
    
    ```
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python:Odoo",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "python": "${command:python.interpreterPath}",
            "console": "integratedTerminal",
            "program": "${workspaceRoot}/odoo-bin",
            "args": ["--config=${workspaceRoot}/odoo.conf", "--dev=xml"],
            "cwd": "${workspaceRoot}",
            "env": {},
            "envFile": "${workspaceRoot}/.env"
        }
      ]
    }
    ```
    
    .vscode/settings.json
    
    ```
    {
    "git.ignoreLimitWarning": true,
    "python.pythonPath": "/Library/Frameworks/Python.framework/Versions/2.7/bin/python",
    "python.analysis.extraPaths": [],
    "python.linting.pylintEnabled": false,
    "python.linting.pycodestyleEnabled": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": false,
    "python.linting.pycodestyleArgs": ["--ignore=E501"]
    }
    ```
