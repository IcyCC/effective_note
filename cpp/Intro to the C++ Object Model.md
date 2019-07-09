
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

主要是增加一个参数 表示对象, 并且换了个民资, 所以 

![例子](../assests/cpp/08.png)

### 虚函数 + 继承




