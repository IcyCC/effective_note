# redis

## 有趣源码的内部机制

### sds

#### embstr vs raw

因为一次分配的内存为 2 的整数倍, redisObject 16 字节, sds 3 字节 留下 44 字节 所以 44 字节以内直接 embstr 44 字节以上 再次分配空间 raw

### 字典

#### 基本结构

dict

```
struct dict {
    dictht ht[2] // 用于rehash
}
```

dictht

```
struct dictht {
    dictEntry** table; // 二维
    long size; // 第一维数组的长度
    long used; // hash 表中的元素个数
}
```

dictEntry

```
struct dictEntry {
    void* key;
    void* val;
    dictEntry* next; // 拉链防止冲突
}
```

### rehash

正常的 rehash 策略:

1. 为 h[1] 分配空间

   - 如果扩容大小等于第一个大于 ht[0].used 的 2 的 n 次方
   - 如果缩容 大小等于第一个大于等于 2 的 n 次方的数

2. 讲 h[0] 的数字 rehash 在 h[1]上
3. 清空 h[0]

渐进式 rehash:

因为 rehash 会阻塞整个 redis, 所以采用渐进式 rehash 进行操作:

1. 为 h[1]分配空间 并且设置 rehashidx 为 0
2. 每次操作 rehashidx + 1
3. 完成(used == 0) rehashidx 清空 s

在渐进 rehash 过程中, 字典的删除, 查找, 更新会在俩个 hash 表进行,
插入会插入到新的 hash 表中

### hash 攻击

利用 hash 函数的偏向性, 降低查询性能

> set 内部由 hash 表实现

