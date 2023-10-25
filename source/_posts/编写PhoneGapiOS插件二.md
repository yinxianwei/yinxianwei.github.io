---
title:  编写PhoneGapiOS插件二
date: {{ date }}
updated: {{ date }}
toc: true
---


    
> 由于要写关于蓝牙的插件，所以方法名里会包含蓝牙关键字，不要奇怪。

#打开工程

- 打开工程如下：
	![QQ20150421-5@2x](media/15027829584942/QQ20150421-5@2x.png)

<!-- more -->

#新建Scheme
<!--more-->
打开并没有办法直接运行，需要创建scheme步骤如下：

- Xcode左上角：

![QQ20150421-14@2x](media/15027829584942/QQ20150421-14@2x.png)

- OK
![QQ20150421-15@2x](media/15027829584942/QQ20150421-15@2x.png)

	
- 成功
![QQ20150421-16@2x](media/15027829584942/QQ20150421-16@2x.png)

	
- 运行和终端结果一样就不上图了。

#新建Plguin类

- 新建OC类`HelloPlguin`继承于`CDVPlugin`

![QQ20150421-8@2x](media/15027829584942/QQ20150421-8@2x.png)

- 导入头文件并创建插件方法

	![QQ20150421-9@2x](media/15027829584942/QQ20150421-9@2x.png)

- 这里我们先不具体实现，只打个Log
![QQ20150421-20@2x](media/15027829584942/QQ20150421-20@2x.png)


#创建JavaScript文件

- 在Finder中查看js文件
![QQ20150421-21@2x](media/15027829584942/QQ20150421-21@2x.png)


- 直接拷贝个已有的`index.js`文件，然后修改文件名为`HelloPlguin.js`
![QQ20150421-6@2x](media/15027829584942/QQ20150421-6@2x.png)

	![QQ20150421-7@2x](media/15027829584942/QQ20150421-7@2x.png)

- 添加方法

	![QQ20150423-1@2x](media/15027829584942/QQ20150423-1@2x.png)

#config.xml配置

- 在`config.xml`中添加方法功能
	
![QQ20150423-2@2x](media/15027829584942/QQ20150423-2@2x.png)

#在index.html调用Plguin方法

- 引入js文件
	![QQ20150423-3@2x](media/15027829584942/QQ20150423-3@2x.png)

	
- 调用
	![QQ20150423-4@2x](media/15027829584942/QQ20150423-4@2x.png)

	
- 由于方法只打了一个LOG，所以没有回调，运行就可以看到log了
	

![QQ20150421-19@2x](media/15027829584942/QQ20150421-19@2x.png)

	


参考：[phoneGap开发IOS,JS调用IOS方法/phoneGap插件开发](https://my.oschina.net/jgy/blog/175643)


