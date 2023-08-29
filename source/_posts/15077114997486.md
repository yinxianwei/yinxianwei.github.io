---
title:  Mac上本地新建SVN步骤
date: {{ date }}
updated: {{ date }}
toc: true
---



![1](media/15077114997486/1.png)

<!-- more -->


![2](media/15077114997486/2.png)
![3](media/15077114997486/3.png)
![4](media/15077114997486/4.png)
![5](media/15077114997486/5.png)
![6](media/15077114997486/6.png)
![7](media/15077114997486/7.png)
![8](media/15077114997486/8.png)
![9](media/15077114997486/9.png)
![10](media/15077114997486/10.png)




4. 启动SVN服务:
`svnserve -d -r  /Users/pengfeishi/Desktop/svn`
特别注意，路径一定是SVN的目录，不是其中一个版本库的目录，不然，能正常启动，就是访问有问题
没有任何输出，则启动成功

5. 关闭: `killall -9 svnserve`

6. 连接: `svn://127.0.0.1/res


