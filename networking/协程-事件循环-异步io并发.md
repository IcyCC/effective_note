# 从协程-事件循环-异步 io 谈并发

当我们讨论异步编程的解决方案 类似 python 的 gevent asyncio 之类的基础库 和 aiomysql 等扩展, 我们总会涉及到 协程, 事件循环, 非阻塞 io 这几个概念. 其实他们是几个没什么关系的东西, 只是 把这些东西 组合起来 成为了现在用的最多的模式.

## 概念

首先是这几个概念:

1.  协程是一个可以保留上下文进行切换的功能

类似

```python

yield
await

```

或者使用 setjump 等方式完成上下文的保存和切换

2.  事件循环就是一个事件机制的循环
    一个简单的实现

```python
class EventLoop(object):
    listener = {}
    event_source = None

    def add_listener(self, event, listner):
        self.listener[event.name] = listener

    def run(self):
        for event in self.event_source.run():
            for l in self.listener[event.name]:
                l(event)
```

3.  非阻塞 io 是 指进行读写等操作, 不阻塞 直接继续运行, 一般会报个错

4.  io 复用, 通过 select 可以查看那些 文件描述符 准备就绪 可以用这个产生事件

知道了这些, 我们可以看看 asyncio 这个包 就是上述内容的组合

- 首先 python 提供了协程的切换的语法 async/await
- 其次 可以使用 eventloop api 进行事件处理
- 内部封装了一个非阻塞的 io 包 并且 把 io 复用的事件放入事件循环

## 其他的模式

既然这几个概念没有关系, 我们可不可以有别的并发模式? 当然可以. 比如

- 单独的协程, 这个一般情况下没什么意义

```
def async_sum(f_id, n):
    res = 0
    for i in range(n):
        res = i+res
        print("Functino id : {} , step: {}".format(f_id, i))
        yield
    return res

a = async_sum(1,3)
b = async_sum(2,4)

next(a)
next(b)
next(a)
next(b)
next(a)
next(b)
```

这个可以让这俩并发的执行

- 单独事件循环

  典型例子 redis

  我们提供了 aeEventLoop 这个事件循环 和 aeCreateTimeEvent 来创建涉及到定时间的任务. 通过不断的更新系统的时间 和 查看最近的任务的时间来进行处理

- 单独事件循环加 + io 复用

  典型例子还是 redis, 还有一票基于 callback 的异步方案

- 其他异步 io

  类似信号+io 复用 也可以实现类似的效果

## 总结

本质上 非阻塞 io+io 复用 减少阻塞, 事件循环让 io 可以操作并发, 协程让异步代码写起来像同步.

针对不同的部分有不同的操作, 比如 协程可以通过各种方法实现 大致分成有栈和无栈俩种(python 有栈 lua 无栈). 通过对协程和事件循环的包装, 可以产生 future 这种更时候使用的对象 等等..
