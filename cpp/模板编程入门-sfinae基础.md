# 模板编程入门-sfinae基础


本文的内容来自 极客时间 [现代C++实战 30 讲](https://time.geekbang.org/column/intro/256?code=TjUT9y8QEechQ9EIIAVu9Kilsx5u1FrzLLQaF8n3X8A%3D), 是对其中内容的一个自己咀嚼后的理解. 

## 基础定义

```c++

template <typename T>
void f(typename T::foo) {
    
}

template <typename T>
void f( T) {

}

```

这个例子里, 如果 T 没有 foo, 当没有 sfinae 的时候, 就会直接编译错误,  因为展开的结果不合法, 不过因为现在有 sfinae 第一个展开发现不合法了不会立刻编译错误, 而是会尝试别的重载展开. 

这个是 sfinae 的基础定义.

## 编译期成员检测

我们有个需求是检测 类是否有 resserve, 类型为 size_t 的对象. 
我们可以写一个 has_reserve 对象, 代码如下

```c++

template <typename T>
struct has_reserve {
    struct good {char dummy;};
    struct bad{   char dummy[2]; };


    template <class U, void (U::*) (size_t)>  
    struct SFINAE{};

    template <class U>
    static good reserve(SFINAE<U, &U::reserve>*)

    template <class U>
    static bad reserve(...);

    static const bool vallue = sizeof(reserve<T>(nullptr) == sizeof(good))
};

```

这个的逻辑就是, 如果 类型 T 有 符合要求的  reserve, 就会选择 good 的重载, 没有就会 bad 根据类型大小的区别可以 在 编译时确定 value 的值

## 利用 enable_if 来阻止展开

利用这个 has_reserve 可以用来配合 enale_if 实现编译期的阻断

看起来形式如下:

```c++

template <typename C, typename T>
enable_if_t<has_reserve<C>::value,
            void>
append(C& container, T* ptr,
       size_t size)
{
  container.reserve(
    container.size() + size);
    ...
}

template <typename C, typename T>
enable_if_t<!has_reserve<C>::value,
            void>
append(C& container, T* ptr,
       size_t size)
{
    ....
}
```

这个的实现原理:

首先 enable_if_t 的实现

``` c++
template< bool B, class T = void >
using enable_if_t = typename enable_if<B,T>::type;
```

获得了一个 enable_if 的 type 字段, 也就是说, 如果他 可以 模板 **展开**, 他就能获得一个 enable_if_t 的 值 就是一个 type,

那么 enable_if 的实现就显而易见了:

成功的时候, 特化

```c++
template<class T>
struct enable_if<true, T> { typedef T type; };
```

根据 enable_if_t 进行展开. type 就是 类型 T.

失败的时候:

```c++
template<bool B, class T = void>
struct enable_if {};
```

没有这个字段, 影响模板的展开, 触发 sfinae 机制, 尝试下一个展开.


## 利用 void_t 标签分发分发


void_t 的定义是这样的.

```c++
template <typename...>
using void_t = void;
```

这个看起来没什么用的模板, 是为了诱导编译器, 检查 void_t<T> 形式的 T的合法性, 来使用 sfinae 机制.

```c++

template <typename T,
          typename = void_t<>>
struct has_reserve : false_type {};

template <typename T>
struct has_reserve<
  T, void_t<decltype(
       declval<T&>().reserve(1U))>>
  : true_type {};

```

这里解释一下, declval 这个东西, 是为了 能让 decltype 在没有默认构造函数的时候使用, 所以 可以先假装 这个就是 decltype,  

这里会检查里面有没有能满足 

```c++
declval<T&>().reserve(1U)
```

没有的话 根据 sfinae 原则, 他不会报编译错误, 而是会接着尝试别的展开. 变成一个 false_type

有了这个机制, 我们就可以利用简单的函数重载,  实现如下代码

```c++

template <typename C, typename T>
void _append(C& container, T* ptr,
             size_t size,
             true_type)
{
    ....
}

template <typename C, typename T>
void _append(C& container, T* ptr,
             size_t size,
             false_type)
{
    ....
}

template <typename C, typename T>
void append(C& container, T* ptr,
            size_t size)
{
  _append(
    container, ptr, size,
    integral_constant<
      bool,
      has_reserve<C>::value>{});
}
```


## 利用  if constexp 做编译时 if

在 cpp 中, 我们不能写如下代码

```c++

template <typename C, typename T>
void append(C& container, T* ptr,
            size_t size)
{
  if (has_reserve<C>::value) {
    container.reserve(
      container.size() + size);
  }

}
```


这是一个运行时的代码, container 没有 reserve , 这个会被编译器的类型检查检查出来, 直接报错...



```c++

template <typename C, typename T>
void append(C& container, T* ptr,
            size_t size)
{
  if constexp (has_reserve<C>::value) {
    container.reserve(
      container.size() + size);
  }
}
```

可以通过如下方法让 这个 if 变成编译时的判断, 根据不同的调节, 展开不同的代码, 这个做法的可读性要比之前的好很多..


## 总结


* sfinae 说白了就是一个机制, **当一个模板展开失败的时候, 会尝试用其他的重载进行展开, 而不是直接报错**,

* 利用这个特性, 我们可以手工诱导发生 sfinae, 来实现编译器的一个类型判断.

* 常见的做法有 enable_if  和 标签分发.

* if constexp 为我们的这种代码增加了更多的可读性 






[1]. 现代 C++30讲: https://time.geekbang.org/column/intro/256?code=TjUT9y8QEechQ9EIIAVu9Kilsx5u1FrzLLQaF8n3X8A%3D



