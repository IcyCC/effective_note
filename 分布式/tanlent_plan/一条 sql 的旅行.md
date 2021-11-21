# 进阶数据库-逻辑优化

> 学习最好的方法就是把他讲给别人。

这是学习， pingcap的 [talent-plan](https://github.com/pingcap/talent-plan) 作业四的学习笔记。 主要讲解优化器相关的知识。

## 逻辑优化的基础

我们有这样一条 sql **select a, max(b) as c from t groub by a having a>1 and c >20**.

这条 sql 经过解析过程成为了一颗 ast 树， ast 树有 sql 的所有信息。 只凭借这课 ast 树， 我们其实是可以执行所有的 sql. 例如我之前学生时代做的大作业， 简易 db ： [chidb](http://chi.cs.uchicago.edu/chidb/index.html) 就是这样的一个数据库。

然而，我们现在要做一个有追求的 db, 就要不仅能用， 还要性能好。

其实这条 sql 有不同的执行方式， 这些执行方式， 这些执行方法和具体的数据库物理实现无关，无论是硬盘型内存型，无论数据分布， 只要按这种方式执行， 就可以获得优化， 这是关系代数保证的。

比如可以先执行 过滤 a>1 再执行 groub by a. 也可以先执行 group by a  再执行 a >1. 这些不同的执行过程的结果是一样的，但是效率天差地别， 如何从这些等价的执行方法中， 选取出最佳的执行方法， 就是逻辑优化要做的事情。

所以我们要对这条 sql 的执行过程做一个抽象， 这个抽象就是 logic plan.

一个逻辑计划由逻辑算子组成。 可以参考 tidb 的[文档说明](https://docs.pingcap.com/zh/tidb/v3.0/query-execution-plan). 他里面定义了如下的算子， 我这里直接引用了 tidb 的[原文](https://pingcap.com/zh/blog/tidb-source-code-reading-7)


> * DataSource 这个就是数据源，也就是表，select * from t里面的 t。
> * Selection 选择，例如 select xxx from t where xx = 5里面的 where 过滤条件。
> * Projection 投影， select c from t里面的取 c 列是投影操作。
> * Join 连接， select xx from t1, t2 where t1.c = t2.c就是把 t1 t2 两个表做 Join。
> * Sort 就是 select xx from xx order by里面的 order by。
> * Aggregation，在 select sum(xx) from xx group by yy中的 group by操作，按某些列分组。分组之后，可能带一些聚合函数，比如 Max/Min/Sum/Count/Average 等，这个例子里面是一个 sum。
> * Apply 这个是用来做子查询的。

他这里用了 sql 举例， 实际上逻辑算子是一层单独的抽象， 他是从关系代数的概念演化而来， 和 sql 的具体语法无关系。  比如聚合算子(Aggregation) 不一定是用 gourp by。 别的一个方法例如 count 也需要聚合算子。

通过这些逻辑算子， 我们就能构造出逻辑计划树。 比如我们的 sql 就可以构造成如下的树.

```
Projection -> Selection -> Aggregation -> DataSource
```

这棵树是**自底向上执行**的.

针对这课逻辑计划树， 我们有一些具体的优化算法

## 逻辑优化算法

tidb 实现了一些具体的逻辑优化算法， 可以参考[这个文档](https://docs.pingcap.com/zh/tidb/stable/sql-logical-optimization). 我这里讲解一下[作业](https://github.com/tidb-incubator/tinysql/blob/course/courses/proj4-part1-README-zh_CN.md)要求实现的谓词下推算法。

谓词下推的思路就是，把过滤的语句提前, 提前减少表的规模. 比如 sql. **select a, max(b) as c from t groub by a having a>1 and c >20**.

这句话正常来看, 应该先 group by 然后进行 having 过滤. 也就是我们默认的这课树.

```
Projection -> Selection -> Aggregation -> DataSource
```

但实际上, a 可以下推到 group by 之前, 这样能减少 group by 的行数. 先  a >1 再 group by a 再 c > 20. 树变成以下形式

```
Projection -> Selection -> Aggregation  -> Selection -> DataSource
```

这样就能减少 group 的行数了.

这里要注意的有两点:

1. 我们的优化是针对每种逻辑算子单独进行的.

例如 group by 中, 能下推的列必须出现在 groub by 的列中. 而 join 的下推方法则是完全不同的.

所以如果你需要实现一个下推优化, 你需要对每一个逻辑算子都重载 **下推** 这个方法. 可以参考[tidb实现代码](https://github.com/pingcap/tidb/blob/master/planner/core/rule_predicate_push_down.go) 感受一下, 每一个逻辑算子节点都有对应的谓词下推实现.

其他的逻辑优化算法也类似, 这里不做过多介绍.

2. 逻辑优化是递归的.

比如谓词下推, 并不是下推一次就行, 我们要不停的下推, 直到不能再下推为止.

例如 **select a from t1, (select c as c1 form t2 groub by c) as t2 where  t2.c > 0**

其中 t2.c 可以先下推到 **select c  form t2 groub by c where c > 0;**
再下推到  **select c  form t2 groub by ( select * from t2 wherec>0);**

所以实现的时候, 每个节点都要判断 上层继承下来的可以下推的条件, 结合自己节点上的条件, 那些可以继续下推, 那些不能.



## 逻辑优化框架

很对一个 sql 的 不同逻辑优化执行方法, 不同的执行顺序, 都可能产生不同逻辑执行计划. 如何从中挑选一个最好的方法? 逻辑优化框架就是解决这个问题的.

一个朴素的思路是, 我们**枚举**出所有的**优化方法**, 从中**挑**一个最优化的.

所以关键步骤就是:

* 枚举
* 优化方法
* 挑

基本思想确定了, 我们就可以看一下 tidb 的优化框架 Cascades 怎么对应这几个概念的.

* 优化方法

在cascades中, 优化方法就是 rule.

一个 rule 能不能用, 取决于其中的Pattern.

比如[作业](https://github.com/tidb-incubator/tinysql/blob/course/courses/proj4-part1-README-zh_CN.md)要求实现的transformation_rules中的 [NewRulePushSelDownAggregation](https://github.com/pingcap/tidb/blob/master/planner/cascades/transformation_rules.go#L584).就是一个 rule, 他的Pattern 就是 要求匹配到 **Selection -> Aggregation**.

如果Pattern可以匹配到, 就可以执行优化规则了.

* 枚举

在 cascades 的框架中, 枚举是通过 memo 来完成的. memo 表达了所有可能的逻辑树的组合. 在执行优化的过程中不断完善.

memo 由 group 和 group expression 组成.

group expression 就是逻辑算子.

group 就是逻辑算子的一个子树结构. 并且 gorup 可以互相引用.

例如 **select * from a join b on a.id = b.id where a >1** 这个 sql.
可以构造以下的 memo (投影省略...):

```
group_list = [
group 0: [
    Selection(a>1) -> gorup 1,

    Join -> group 2
        -> group 3
]
group 1: [
    Join->group3
        ->group4
],

group 2: [
    Selecttion(a>1)->group3
],
group 3: [DataSource(a)],
group 4: [DataSource(b)]
]
```

通过以下的 memo 我们可以看到有 .

```
gourp1[0] -> group2[0] -> group3[0]
                       -> group4[0]
```

和

```
gourp1[0] -> group2[0] -> group3[0]
                       -> group4[0]
```

这几种逻辑执行计划.

在执行过程中不断生成的 group 加入 memo, 便完成了枚举操作.

这里可以发现, 我们自顶向下求解的过程中, 有一些 子group的 的最优结构是计算过的.
如果一个group 是枚举过的, 那么之后就无需再枚举该 gourp 了.这就是最优子结构, 可以使用 dp 方法. memo 就是我们的备忘录.

```
memo[group] = best(memo[group-1] apply rules)
```

所以我们要做的就是, 从根节点出发, 不停的找到可以使用的 rule. 使用规则产生新的 group 的路径, 加入 memo.


可以参考这里的 [代码](https://github.com/pingcap/tidb/blob/7755d25aba5120dafde98fff11ab3b98ca4d192f/planner/cascades/optimize.go#L138)

这样我们就的到了所有的优化过的逻辑子树.


* 挑

之后根据统计信息, 就可以对比挑选了. 这里下节再说

## 参考资料

[1]. 揭秘 TiDB 新优化器：Cascades Planner 原理解析 https://pingcap.com/zh/blog/tidb-cascades-planner

[2]. TiDB 源码阅读系列文章（六）Select 语句概览 https://pingcap.com/zh/blog/tidb-source-code-reading-6

[3]. TiDB 源码阅读系列文章（七）基于规则的优化 https://pingcap.com/zh/blog/tidb-source-code-reading-7

[4]. tinysql 作业四 https://github.com/tidb-incubator/tinysql/blob/course/courses/proj4-part1-README-zh_CN.md

[5]. tidb 文档 https://docs.pingcap.com/zh/tidb/v3.0/query-execution-plan