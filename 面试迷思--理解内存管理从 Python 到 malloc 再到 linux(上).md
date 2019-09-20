写这个的也是面试官的一道题, 问 python 中内存是怎么分配的, 其实这个问题是一个很复杂的问题, 因为涉及到好多个层次, 分别包括:

* Python 对象内部的内存管理 
* **Python 虚拟机的内存管理 (memory allocator)**
* **malloc 内存管理**
* linux 的内存管理

这次就从机制上, 用代码, 介绍一下这几层内存管理的大致实现.

阅读的过程中, 可以重点关注单独自己层要解决的和其它层不一样的问题和他与其他层的相似之处.

##  Python 内部对象的内存管理 

这里能说的比较少, 每个对象的面临的场景不一样, 简单来说, 比如 Python 的 List,
list 每次发现容量满了的时候, 都会预先申请一些空间,  我们在 Objects/listobject.c 中  的 repr 方法里查看一下 list 的状态 

![image.png](http://note.youdao.com/yws/res/4875/WEBRESOURCEa7f4d3cb2207c07830eb03252895ae3d)

这样 每次打印的时候 就能看的 list 状态

试一下

![image.png](http://note.youdao.com/yws/res/4879/WEBRESOURCEbcba5c48064932422c616bbf814a0a03)

可以看到 只插了一个元素 却申请了 4 个元素空间

![image.png](http://note.youdao.com/yws/res/4881/WEBRESOURCEadee6576094428a9dd5b0f80c719de1c)

在插了到了 5 个元素空间变成了 8

其实其他的对象也有类似的机制, 会提前申请大一些的内存, 用来插入. 这样的目的也是减少从下级的内存分配器申请内存

那我们申请内存的下一级在哪里呢?

我们看 listobject.c 的代码 

我们看到
![image.png](http://note.youdao.com/yws/res/4898/WEBRESOURCE8afe65c255575229543dd1d4940c18dc)

大致猜想一下, PyObject_GC_New 这个应该就是下一层的内存分配器的接口, _PyObject_GC_TRACK 这个应该是处理垃圾回收的 暂时不管

## Python 虚拟机的内存管理 (memory allocator)

不断的紧跟函数调用关系 在Objects/obmalloc.c 中 我们发现了 
![image.png](http://note.youdao.com/yws/res/4902/WEBRESOURCE6f4d1a7b7be45d388b2675ff4d8219cf)

这个, 这个应该是 python 垃圾分配器的接口,  看了一堆麻烦的调用关系以后,
![image.png](http://note.youdao.com/yws/res/4910/WEBRESOURCEa8aa3fe18a7e7aad42c969003346b110)
我们 找到了这个接口的实现, 首先他也是分层的, 分为 raw 和 mem, obj 三层, 由于 mem,obj用的一个分配器, 我们把它当做一个来看, 去看一下 PYMALLOC_ALLOC的实现

可以看到 

![image.png](http://note.youdao.com/yws/res/4920/WEBRESOURCEcb0601cddb2145f6d4403beff6b7c5a3)

红线一组目测就是我们要的东西 
![image.png](http://note.youdao.com/yws/res/4922/WEBRESOURCE445e9cb839e786fecf13327db23ed697)

点开发现 同样的思想又来了, 先看看能不能申请成功不能就去下一层, 下一层就是我们的刚刚看到的 raw_alloc 跟一下看到了

![image.png](http://note.youdao.com/yws/res/4927/WEBRESOURCE77c46d43d18adac805e87c994eebae16)

熟悉的 malloc 这里就不管了, 我们把重点放在
