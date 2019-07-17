# code

是一个代码段, 一个函数,模块,类, 迭代器

## 字段:

* co_argcount 参数个数
* co_stacksize 栈空间
* co_nlocals 局部变量数量
* co_code 字节码

# frame

栈帧, 一个执行环境 用  sys._current_frames() 获得

## 字段:

* f_values/ f_stacktop... 栈的位置
* f_back 前一个栈帧

## 机制:

* 复用, 代码相同的栈帧不会构造直接复用

# gil

释放:
只有一个线程, 不会释放 gil
等待 gil 的线程看到 gil 为 1 直接申请要, 持有的下次执行释放, 超时的置为 0 重新等待
条件变量获取线程


# 内存管理

# arean 链表 256k
# pool 4kb
# block 