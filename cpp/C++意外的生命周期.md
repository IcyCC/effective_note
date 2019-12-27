# C++ 意外的生命周期

## 什么是对象?

对象类型就是 一个 不是 函数, 不是 引用, 不是空的 类型.

## 生命周期

开始: 一个对象被非空初始化的时候

结束: 一个对象被 重要的析构 析构 或者 占据的空间被释放


### 引用没有生命周期

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227110523.png)

第一个没什么可说的


![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227110707.png)

第二个可以看出, 引用没生命周期

>  [[maybe_unused]] 取消对没有使用的 warnning



### 用标准库简单包裹一下, 会引发编译器识别错误

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227111428.png)

返回一个 local 的 refrence 是一个未定义的行为,
一般会给警告, 返回了一个 stack memory 类似的

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227113108.png)

也是一个未定义行为. 不过大部分编译器不会给警告

## 例子

### 字符串

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227113713.png)

这个一切正常, 因为字面量在 static 段

**重点: 字面量的生命周期比想的长,**

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227113933.png)

> string_view 是一个简单的指针

这个一切正常

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227114051.png)

这个是一个未定义行为, 实际上返回了stack 的 内存, 不会得到 warning, 但是会乱码或者不输出..

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227114614.png)

这个一切没有警告, 打印了空, 因为 s 是一个数组 在 stack 上

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227115957.png)

这样就正常了 可以输出, 因为指向了 常量区

**重点:  字符串数组不长**: 

### 容器

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227115518.png)

结果:

```
S(int)
S(&&)
~S()
~S()
```

**重点: move 后的对象仍然需要析构, 所以在析构的时候要判断一下是否重复清理**


### 临时量

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227120536.png)

结果:

```
S()
"Hello World"
~S()
```

**重点: 临时量的生命周期 可以通过给一个引用来延长**


![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227121454.png)


返回值是 1 , m 被正常的初始化了

**重点: 临时量的生命周期延长是可以递归的起作用**


### 列表初始化

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227122215.png)

这个是 1 次内存分配, 因为 使用了 **小字符串优化** . 所以只有 vector 的内存..


![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227122320.png)

这个是 5 次分配,  

> initializer_list 的实现方式是 创建了一个预期类型 const 的隐藏数组 的 数组

所以 先建立了一个数组 const string, 分配了俩个空间,  然后 vector 一个空间之后, 建了俩个string空间,  拷贝过去

**重点: initializer_list创建隐藏数组**

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227172022.png)

这个分配 0 次, 可以认为是 std::array<const char *, 2>


std::array 实现方式类似

```
template<typename T, std::size_t Size>
struct array 
{
    T _M_elems[Size];
}
```

所以没用 initializer_list, 他会直接褚淑华内部的数组.


**重点: std::array<> 没有构造函数 多使用不同参数的构造函数**

## for

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227173119.png)

未知行为, 因为这个语句展开

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227173547.png)

auto && 只会延长 get_s() 的生命周期 ,不会延长 get_data() 的生命周期,


**重点: range-for loop 会创建影藏变量, 所以要考虑他们的生命周期**



### RVO 返回值优化

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227174124.png)

打印结果

```
S()
~S()
```
因为触发了 RVO.

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227174240.png)

这个在 C++17 以后就支持了 所以结果同上

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227174356.png)

这个会触发 NRVO 所以 也同上

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20191227174640.png)

这个是

```
S()
S(S&&)
~S()
~S()
```

返回值触发了 RVO, 所以没有额外构造, 赋值的时候触发了移动构造

**重点: 编译器会自己处理右值的移动**
