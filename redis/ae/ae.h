#include <time.h>

// 一些函数的定义
typedef void aeFileProc(struct aeEventLoop *eventLoop, int fd, void *clientData, int mask);
typedef int aeTimeProc(struct aeEventLoop *eventLoop, long long id, void *clientData);
typedef void aeEventFinalizerProc(struct aeEventLoop *eventLoop, void *clientData);
typedef void aeBeforeSleepProc(struct aeEventLoop *eventLoop);

typedef struct aeFileEvent
{
    int mask; // 捕获的掩码 读/写
    aeFileProc *rfileProc;
    aeFileProc *wfileProc;
    void *clientData;
} aeFileEvent;

/* 准备就绪的事件 */
typedef struct aeFiredEvent
{
    int fd;
    int mask;
} aeFiredEvent;

typedef struct aeTimeEvent
{
    long long id;         /* time event identifier. */
    long when_sec;        /* seconds */
    long when_ms;         /* milliseconds */
    aeTimeProc *timeProc; // 处理
    aeEventFinalizerProc *finalizerProc;
    void *clientData;
    struct aeTimeEvent *next; // 链表
} aeTimeEvent;

typedef struct aeEeventLoop
{
    /* data */
    int maxfd;                 // 注册的最大的文件描述符
    int setsize;               // 关注的最大文件描述符数量
    long long timeEventNextId; // 下一个timer 的 ID
    time_t lastTime;           // 诊断系统时间差
    aeFileEvent *events;       // 关注的event
    aeFiredEvent *fired;
    aeTimeEvent *timeEventHead;     // 链表链接时间事件
    int stop;                       // 运行状态
    void *apidata;                  //特别数据
    aeBeforeSleepProc *beforesleep; // 钩子 下个事件发生执行
} aeEeventLoop;

