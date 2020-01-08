# 聊聊boost--Operators和继承链

本次内容来自 [boost文档](https://www.boost.org/doc/libs/1_72_0/libs/utility/operators.htm) 

Operators 是一个辅助写运算符重载的 lib, 包括几个大部分: 

* 单个参数运算符标准定义的简单生成
* 通过俩个参数的模板 生成
* 基于数学的群的定义, 的模板
* 迭代器模板

这些会拿来和标准库的 [rel_ops](https://en.cppreference.com/w/cpp/utility/rel_ops/operator_cmp) 做个对比

用到了一个好玩的技术就是 **基类链**

## Operators

### 单个参数的运算符

```c++
class MyInt
    : boost::operators<MyInt>
{
    bool operator<(const MyInt& x) const;
    bool operator==(const MyInt& x) const;
    MyInt& operator+=(const MyInt& x);
    MyInt& operator-=(const MyInt& x);
    MyInt& operator*=(const MyInt& x);
    MyInt& operator/=(const MyInt& x);
    MyInt& operator%=(const MyInt& x);
    MyInt& operator|=(const MyInt& x);
    MyInt& operator&=(const MyInt& x);
    MyInt& operator^=(const MyInt& x);
    MyInt& operator++();
    MyInt& operator--();
};
```

继承了一个 operator<T>, 按照要求填写这些, 就可以生产剩下所有的运算符, 这个用起来比较麻烦, 一写得写一堆.

### 标准库 rel_ops

```c++
struct Foo {
    int n;
};
 
bool operator==(const Foo& lhs, const Foo& rhs)
{
    return lhs.n == rhs.n;
}
 
bool operator<(const Foo& lhs, const Foo& rhs)
{
    return lhs.n < rhs.n;
}
 
int main()
{
    Foo f1 = {1};
    Foo f2 = {2};
    using namespace std::rel_ops;
 
    std::cout << std::boolalpha;
    std::cout << "not equal?     : " << (f1 != f2) << '\n';
    std::cout << "greater?       : " << (f1 > f2) << '\n';
    std::cout << "less equal?    : " << (f1 <= f2) << '\n';
    std::cout << "greater equal? : " << (f1 >= f2) << '\n';
}
```

实现 一个 < 和 == 通过 rel_ops 可以实现出其他的运算符, 原理就是用这俩个运算符实现别的运算符

### 俩个参数的模板

例子

```c++
template <class T>
class point    // note: private inheritance is OK here!
    : boost::addable< point<T>          // point + point
    , boost::subtractable< point<T>     // point - point
    , boost::dividable2< point<T>, T    // point / T
    , boost::multipliable2< point<T>, T // point * T, T * point
      > > > >
{
public:
    point(T, T);
    T x() const;
    T y() const;
    point operator+=(const point&);
    point operator-=(const point&);
    point operator*=(T);
    point operator/=(T);

private:
    T x_;
    T y_;
};
```

继承一个模板类  如这个 less_than_comparable<T> , 实现他要求的接口, 就能自动实现满足这个性质的运算符..

注意看

```c++
boost::addable< point<T>          // point + point
    , boost::subtractable< point<T>     // point - point
    , boost::dividable2< point<T>, T    // point / T
    , boost::multipliable2< point<T>, T // point * T, T * point
      > > > >
```

这个代码 , 看起来有点奇怪, 稍后讲干啥的

### 群论描述

是对上一个模式的封装, 把常用的模式进行组合, 理论基于群论..

类似 totally_ordered<T> 就是对 less_than_comparable 和 equality_comparable 的组合封装. 没啥好说的

### 迭代器

这个部分有意思的是:

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20200108123650.png)

可以通过这个看出来迭代器类型的关系, 当你继承了这个的时候, 就等于继承他所组合的 俩个参数的运算符模板.

这里比较让人困惑的是 xxx_iteratable 和 底下xxx_iterator_helper 的关系

简单看一下代码 以 input_iteratable 为例子

首先, 

```c++
template <class T, class P, class B = operators_detail::empty_base<T> >
struct input_iteratable
    : equality_comparable1<T
    , incrementable<T
    , dereferenceable<T, P, B
      > > > {};
```

这个的定义比较简单, 就是一个继承了之前说到的运算符的东西.

接下来看到一个基类, 所以有的 xx_iterator_helper 都会继承这个

```c++
template <class Category,
          class T,
          class Distance = std::ptrdiff_t,
          class Pointer = T*,
          class Reference = T&>
struct iterator_helper
{
  typedef Category iterator_category;
  typedef T value_type;
  typedef Distance difference_type;
  typedef Pointer pointer;
  typedef Reference reference;
};
```

其实就是 stl 的 iterator_traits.

最后看 helper 的实现

```c++
template <class T,
          class V,
          class D = std::ptrdiff_t,
          class P = V const *,
          class R = V const &>
struct input_iterator_helper
  : input_iteratable<T, P
  , iterator_helper<std::input_iterator_tag, V, D, P, R
    > > {};
```

感觉上就是给了 help 的 iterator_category 类型做了个确定. 我们用的时候只要继承特定的 help 就可以确定迭代器的类型和要实现的内容了.

> 完了 这里感觉没太看懂, 有老哥看懂了加一下哦....


### 基类链

这个代码


```c++
boost::addable< point<T>          // point + point
    , boost::subtractable< point<T>     // point - point
    , boost::dividable2< point<T>, T    // point / T
    , boost::multipliable2< point<T>, T // point * T, T * point
      > > > >
```

首先, 这么写的目的是为了规避多继承, 为什么规避多继承呢?

可以参考 [C++多继承有什么坏处，Java的接口为什么可以摈弃这些坏处？修改](https://www.zhihu.com/question/31377101/answer/404546399) 的回答

主要是

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20200108130000.png)

这个原因.

他提到的 Template parameter as Base Classes 就是这个东西.


那这个操作怎么实现的呢?

```C++
template <class T, class B >
class MyClass : public B{}; 
```

原理都很简单, 一看就懂, 不过这个技巧要好好掌握.



