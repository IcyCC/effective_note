
# C++ 对象模型简介

> 来源 https://www.youtube.com/watch?v=iLiDezv_Frk 的视频

## POD(plain old data)



![例子](../assests/cpp/01.png)

c的内存布局, 字段从下到上占据从高到底位置的内存


## CPP

### 原始

![例子](../assests/cpp/02.png)

这个是和 pod 等价的只是访问权限不同


### 简单继承

![例子](../assests/cpp/03.png)

原因如下

![例子](../assests/cpp/04.png)


### 带有函数

![例子](../assests/cpp/05.png)

类是如何处理成员函数?

![例子](../assests/cpp/07.png)

主要是增加一个参数 表示对象, 并且换了个名字, 所以 

![例子](../assests/cpp/08.png)

### 虚函数 + 继承

![例子](../assests/cpp/09.png)

编译器是如何处理这个的?

首先我们看这么一个调用

![例子](../assests/cpp/10.png)

编译器会转换成如下的格式

![例子](../assests/cpp/11.png)

1. 增加一个 vtable 的指针 指向一个 tbl 
2. 具体实现放入 tbl
3. 调用的时候通过 vtable 偏移 为 tbl 中函数所在的位置


当我们有个继承类的时候, 内存布局如下:
![例子](../assests/cpp/12.png)

那我们怎么决定 vtable 指针的指向呢? 答案是靠 构造函数

![例子](../assests/cpp/13.png)

每个构造函数里会添加:
1. 父类的构造
2. 修改 vtable 指向, 指向一个常量

> 所以 构造函数中不可以调用虚函数, 尤其是父类, 因为此时 vtable 没有初始化, 会导致指向错误, 调用错误的函数

