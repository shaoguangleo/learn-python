# 我们编程吧 之 python 学习手册
**Version 0.2**



# Python库

## Numpy

**NumPy**系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。据说NumPy将Python相当于变成一种免费的更强大的MatLab系统。

 - 快速高效的多维数组对象ndarray
 - 对数组进行运算的函数
 - 读写硬盘上基于数组的工具
 - 线性代数、傅里叶变换以及随机数生成
 - 用于将C、C++、Fortran代码集成到Python的工具

## pandas

Python Data Analysis Library 或 **pandas** 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

Pandas中的数据结构

 - Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。
 - Time- Series：以时间为索引的Series。
 - DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。以下的内容主要以DataFrame为主。
 - Panel ：三维的数组，可以理解为DataFrame的容器。

## matplotlib

[matplotlib](www.matplotlib.org/ "matplotlib")是最流行的用于绘制数据图表的Python库。非常适合创建出版物上用的图表。跟IPython结合的很好，提供了一种非常好用的交互式数据绘图环境，绘制的图表也是交互式的，你可以利用绘图窗口中的工具栏放大图表中的某个区域或对整个图表进行平移浏览。

## ipython

ipython 是Python科学计算标准工具集的组成部分，是一个 python 的交互式 shell，比默认的python shell 好用得多，支持变量自动补全，自动缩进，支持 bash shell 命令，内置了许多很有用的功能和函数。

除了标准的基于终端的IPython shell外，该项目还提供了：

 - 一个类似Mathematica的HTML笔记本
 - 一个基于Qt框架的GUI控制台
 - 用于交互式并行和分布式计算的基础架构

## SciPy

SciPy是一款方便、易于使用、专为科学和工程设计的Python工具包。

它包括

 - 统计
 - 优化
 - 整合
 - 线性代数模块
 - 傅里叶变换
 - 信号和图像处理
 - 常微分方程求解器等等


# 更多信息
Hi，XDJM们，更多信息欢迎移步[我的github](https://github.com/shaoguangleo)或微信公众号letsProgramming.

![letsProgramming](http://img.blog.csdn.net/20160128231400788)
