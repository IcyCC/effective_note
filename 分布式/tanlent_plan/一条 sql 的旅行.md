# 从数据库看一条 sql 的旅行 -- 总论

前言 最近在做pingcap 的 talent-plan 这里对学习到关于sql 执行过程的知识点做一个总结。

学习一个东西最好的方法， 就是把一个东西讲给别人。

接下来， 我会以 **select a, max(b) from t groub a having a > 1;** 这句 sql为例子来说明

## 解析（Parsing）

第一步是解析， 把文本的 sql 语言翻译成程序的 ast 结构。

这里涉及到一些编译原理的知识， 包括词法分析， 语法分析等。 这里不做过多的介绍，可以学习一下编译原理的基础知识， 
最终， sql 会变成一颗 ast树， 里面包含了 sql 语句所表示的所有信息。

一个的结构可以参考 https://github.com/pingcap/tidb/blob/source-code/ast/dml.go#L451

```
type SelectStmt struct {
        dmlNode
        resultSetNode
        // SelectStmtOpts wraps around select hints and switches.
        *SelectStmtOpts
        // Distinct represents whether the select has distinct option.
        Distinct bool
        // From is the from clause of the query.
        From *TableRefsClause
        // Where is the where clause in select statement.
        Where ExprNode
        // Fields is the select expression list.
        Fields *FieldList
        // GroupBy is the group by expression list.
        GroupBy *GroupByClause
        // Having is the having condition.
        Having *HavingClause
        // OrderBy is the ordering expression list.
        OrderBy *OrderByClause
        // Limit is the limit clause.
        Limit *Limit
        // LockTp is the lock type
        LockTp SelectLockType
        // TableHints represents the level Optimizer Hint
        TableHints [](#)*TableOptimizerHint
}
```

假设你的 数据库的语法比较简单， 也不准备做什么特别的优化， 通过 ast 的信息， 你就可以直接完成数据库操作， 实现一个简单的数据库了。

如果你对剩下的优化内容不感兴趣，
那么你可以做一下 [chidb项目](!http://chi.cs.uchicago.edu/chidb/index.html)。

不过， 我们是一个有追求的 db, 我们希望做到更优， 那就需要接着往下看了。

## 优化

同样的一句 sql， 不同的执行方法效率会天差地别。 从能达到相同结果的不同的执行方式中选取一条最佳的方式就是优化。

我们可以从两条路线优化我们 sql 执行；

* 一条是更改操作的执行顺序， 比如我们可以先执行 where 的 filter 再执行 group by ， 还可以把投影选取列提前等方式进行优化。 这些优化和具体的db 实现没有关系， 是关系代数决定了优化的正确性。

* 另一种是选取不同的执行方式， 比如是否走索引， 用什么 join 算法等，这就是从物理实现上考虑的优化

第一种我们称之为逻辑优化， 第二种称之为物理优化。

### 逻辑优化

### 物理优化


## 执行






