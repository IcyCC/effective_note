
# 数据复制

## 主从复制:
只有主节点可写的

## 同步和异步复制
是否等从节点确认

## 不停机配置新的从节点流程:
1. 对主节点进行一致性快照
2. 快照到新节点
3. 向主节点请求快照点位置之后所有日志
4. 进行处理

## 节点切换
1. 确认失效
2. 选举新的主节点
3. 配置新的节点
问题:
1. 异步复制, 新节点成为主节点时, 旧节点比新节点数据新. 旧节点给新节点同步数据冲突. 
2. 基于问题 1, 如果丢弃数据会导致外部系统不一致. 如同一个 key 的数据缓存和 db 不一致.
3. 两个节点同时成为主节点 发生脑裂
4. 如何检测主节点失效?

## 复制日志的实现

1. 语句级别: 存在非确定函数, 自增列数据, 副总用函数的问题
2. wal 日志: 泰国底层, 贴近物理描述
3. 逻辑日志: 解耦逻辑日志和物理日志

## 复制滞后

写后读一致性
* 强制从主节点
* 记录更新时间, 看时间范围决定是否从主节点读

## 单调读
用户看到的值不会比之前看到的值更旧， 实现用哈希到固定的分库

## 一致前缀读
由于不同分区延迟不同 导致写入的前后不同破坏了因果性
要保证因果性相关的写入一个分区。

## 多主复制

问题： 多主写入的数据冲突。
* 避免冲突 通过路由让一个用户的数据只访问一个主
* 收敛到一致 例如 保留最后一个方式 或者 记录流水业务处理
* 自定义业务冲突 写执行 读执行

拓扑结构：
1. 环状 2. 星型 3. 全连接

## 无主复制

核心思想： 法定人数 多份写入 多份读


# 数据分区

## 分区方法

* 关键字区间: 支持高效查询, 哈希分区
* 哈希分区: 分布均匀.

## 二级索引

基于文档: 每个分区独立 便于写入
基于词条: 便于读取

## 分区平衡

取模: 会导致每次扩展都有很多 key 需要迁移
固定数量分区: 把分区数量定高, 之后再平衡分区, key 的计算分区是固定的, 只会动这些分区.
动态分区:  类似一致性哈希的思想

## 请求路由
* 中心化调度: zookeeper
* gossip: 类似路由协议 每个节点负责转发

## 事务

### 脏读
读到了另一个事务未提交的内容
防止脏读： 读提交
危害：1.多对象更新，防止外界观察到部分更新 2.事务回滚， 防止发现写入的事务。
实现： 语句级别的快照。

## 脏写

未提交的写入被另一个事务覆盖。
危害： 1. 一个事务的两个写入操作 被其他事务覆盖其中一个写入操作造成不一致。
解决方法： 行级别写锁

## 不可重复读

一个事务开始后， 两次读取结果不一样。
危害： 出现短暂的不一致。 备份场景， 数据分析场景 不接受不一致。
解决方法：  mvcc 事务级别快照。

## mvcc 索引优化

## 幻读
危害： 认为自己修改了要修改的全部数据
解决方式： 间隙锁

## 串行化

* 2pl协议 事务开始不断上锁， 事务结束不断释放锁

# 共识和一致性

### 可线性

让系统看起来只有一个副本

> 区分线性化和串行
> 串行: 事务执行的顺序看起来和串行执行差不多
> 线性: 每次读取单个对象的最新值

目标: 满足约束 一旦读返回了新值 后续所有的读操作都要返回新值

必须线性化的场景
* 主节点选取时分布式锁: 必须保证只有一个主节点
* 约束和唯一约束: 类似锁
* 存在不同的传输通道需要保持一致

### 实现

* 主从复制(部分线性化): 保证从主节点上读数据可以线性化
* 共识算法(可线性化): 
* 多主复制(不可线性化): 多个节点并发写入 存在冲突
* 无主复制(可以认为不线性化): (r + w > n) 存在网络延迟可能不线性化

### 代价
网络延迟, 就没有可用性 代价.

## 顺序保证

### 因果全序并非全序

#### Lamport 时间戳 

> (操作号, 节点号) 每个节点保存自己见过最大的编号

每个节点看完新的就不会看旧的

## 分布式事务和共识

### 两阶段提交(2pc)

先问节点能不能接受 节点一旦承诺能接受就要必须完成.

无法处理协调者崩溃.

关键点: 协调者可用性


### 共识

共识算法: 一个或者多个节点提议值, 共识算法决定最终值

满足性质:

* 协商一致: 节点接受相同提议
* 诚实: 节点不能反悔
* 合法: 值 v 是由某个节点提议的
* 可终止: 最终一定能打成决议

2pc 不满足 可终止性(协调者故障)

实际使用中会用全序广播, 一次决定多个值

主节点唯一比较困难, 共识算法往往只保证每个世代的主节点唯一
和 2pc 对比, 2pc 需要所有节点都返回是, 共识只需要大部分节点返回是

#### 局限性

好处: 一致性, 完整性, 有效性, 支持容错(大多数节点工作) 
代价:

* 节点投票是同步复制, 性能有损耗
* 分区故障会导致少数节点所在分区不可用
* 扩容繁琐
* 无法准确监控主节点异常 (对网络敏感)

## 协调服务

zookeeper

* 任务分配
* 服务发现
* 成员服务








