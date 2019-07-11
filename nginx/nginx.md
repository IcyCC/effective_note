# Nginx

## 使用

###  热升级

步骤
1. 备份 
```
cp nginx nginx.bak
```

2. 发送 USR2

```
kill -USR2 pid
```

此时nginx 新老都在

3. 发送 -WINCH 

```
kill -WINCH pid
```

此时老的work退出 master还在 可以通过 reload 来启动

### 日志切割

使用 reopen 开启新的日志

## 内部机制

### 进程结构

* 分为 master worker cacheManager(管理) cacheLoader(载入) 
* 基于共享内存通信 

### 进程管理

* master

```
监控 worker CHLD 重启
管理 worker
```


## 网络事件

读事件:

* Accept
* Read
* 对端关闭

写事件:

* 写消息


## 连接池

## work通信

