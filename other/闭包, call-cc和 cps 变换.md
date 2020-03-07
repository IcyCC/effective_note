# 关于闭包, call/cc和 cps 变换

本文是对知乎文章, [柯里化的前生今世](https://zhuanlan.zhihu.com/p/34060802) 的一个学习笔记.  旨在用简单的人话说清楚上面的概念, 不做深入的研究!!!!


## 闭包

> 这里用 js 语法举例子 不是 js 的运行时特性

理解闭包要先理解 作用域, 作用域就是其中的符号是指什么.

```js
let x = 1;

let foo = ()=>{
    return x;
}

let bar = () => {
    let x = 10;
    return foo()
}

```

我们看这个函数, 当我们执行

```js
bar()
```

的时候, 其实有俩种理解. 

第一种是所谓的 **动态作用域** x 是 10, 原因

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20200304115300.png)

系统的作用域查找情况如下, 当执行到 foo 的时候, 开始找 x, foo 里没有, 就向 bar 找, bar 的 x 是 10, 所以 x 就是 10


另一种就是**词法作用域** x 是 1, 原因

![](https://gitee.com/IcyCC/PicHouse/raw/master/assests/20200304120600.png)

foo 的作用域会存一下 **定义 foo 时的作用域信息**, foo里找不到, 会在定义 foo 的作用域里找.

所谓闭包就是 **保存定义函数时的作用域**.

当我们在 lisp 中, 实现 lisp 解释器的这个功能的时候, 思路如下:

我们先定义好在作用域中找 symbol 的函数

```lisp
(define (get-symbol-value env key)
  (let lookup-env
    ((env env))
    (if (null? env)
        (error 'get-symbol-value "failed to find symbol")
        (let ((head-frame (car env)))
          (if (hash-has-key? head-frame key)
              (hash-ref head-frame key '())
              (lookup-env (cdr env))))))) ;; 核心是这句, 如果找不到不断向上一个栈帧找.

```

首先是动态作用域:

```lisp
(define (eval-function-call-list exp)
  (display "eval-function-call-list\n")
  (let* ((fn (eval-exp (car exp)))
         (arg (eval-exp (cadr exp)))

         (body (function-body fn))
         (param (function-param fn))

         (frame (create-frame)))

    (extend-frame frame param arg)

    (let* ((env *env*)
           (value '()))
      (set! *env* (extend-env *env* frame)) ;; 压入当前要调用函数的栈帧(作用域)
      (set! value (eval-exp body))
      (set! *env* env) ;; 弹出当前要调用函数的栈帧(作用域)
      value)))
```

这个是的思路很简单, 每次调函数都会把当前函数的栈帧压进去, 执行弹出来.


词法作用域呢?

```lisp


(define (eval-lambda exp env)  
  (display "eval-lambda\n")  
  (let ((param (caadr exp))        
        (body (caddr exp)))    
    (closure param body env))) ;; 把当前定义该函数的作用域保存起来

(define (eval-function-call-list exp env)  
  (display "eval-function-call-list\n")  
  (let* ((clos (eval-exp (car exp) env))         
         (arg (eval-exp (cadr exp) env))

         (body (closure-body clos))
         (lexical-env (closure-env clos)) ;; 拿出当前的函数保存的词法作用域
         (param (closure-param clos))

         (frame (create-frame)))

    (extend-frame frame param arg)
    
    (let ((executing-env (extend-env lexical-env frame)))  ;;; 把当前的作用域压上去
      (eval-exp body executing-env)))) ;; 用这个执行 参考上面的图
```

有了词法作用域我们可以干什么? 

**用函数实现对象.**

```lisp
(define let-create-obj
    (let ((hidden 5))
      (lambda ()
        (let ((state 1))
          (list
           (lambda () (+ hidden state))
           (lambda (v) (set! state v)))))))

(define obj1 (let-create-obj))
(define obj1-get-state (car obj1))
(define obj1-set-state (cadr obj1))
```

就是用闭包封装创建时候的作用域, 来通过函数操控. 这个思路我们


## call/cc

call/cc 是一个函数, 用处是 *注册一个单个参数的**回调**, 在求值的时候 把当前的解释器执行的过程, 作为这个函数的参数传进去 , 并且这个回调用时候的参数,作为这个 call/cc 表达式求值的结果* : 

让我们举个🌰:

```lisp

(+ (call/cc (lambda x : (x 2))) 4)
```

比如这句话,  我们执行到 

我们可以这样理解 对

```lisp
(call/cc (lambda x: (x 2)))
```

求值, 可以看做在 call/cc 的时候, 把求值环境作为 x传入, 当 x 以  2 为参数的时候, 这个表达式返回值为 2 所以是 答案是 6

我们看一个复杂的情况, 用 call/cc 实现 yield, 

```lisp

(define (gen x)
  (define k-body #f)
  (define k-yield #f)

  (define (yield x)
    (call/cc (lambda (k2)
               (set! k-yield k2)
               (k-body x))))

  (lambda ()
    (call/cc (lambda (k1)
               (if (eq? k-body #f)
                   (begin
                     (set! k-body k1)
                     (yield x)
                     (yield (+ x 1))
                     (+ x 2))
                   (k-yield))))))

(define iter (gen 1))
(iter)  ;1
(iter)  ;2
(iter)  ;3
```

yield 的本质是切换上下文, 所以这段代码可以这么理解:

1. gen 利用闭包所学的知识, 可以发现是一个拥有 call 方法的累
2. 构造一个 iter 对象
3. 调用的时候, 还按之前的理解, 在 call/cc 处中断, 准备看k1 什么时候调用
4. k1 没有被调用, 被保存到了 k-body, 并 通过 yield x进入了下一个 call/cc
5. 准备看k2 什么时候调用, k2被保存到了 k-yield, 这时候 k-body 也就是k1 突然被调用, 返回到第一个 call/cc 出 结果是 x, 所以第一个 yield 为 x
6. 进行下一个 iter调用, 因为这时候 k-body 不为空, 所以直接调用k2 返回 yileld 处, 无返回值
7. 继续运行,重复上述步骤

从这里, 我们可以看出, 利用 call/cc 能封装当前调用环境并且闭包到下一个 call/cc 的性质, 可以实现对某个执行状态的保存, 实现上下文的切换

### call/cc 是怎么实现的?

可以有俩种思路实现它.

第一种是暴力做法,  
我们把 call/cc 看做一个接受一个参数 为 (参数为一个参数的回调) 的函数,可以用 setjump 和 longjump 这种手段实现它, 思路类似:

```js
let call_cc =  (cb) => {
  setjump
  cb((arg)=>{longjump(arg)})
}
```

这个一看就懂不做解释.

第二种是一个利用纯函数的办法, **我们可以显式的用函数表示函数返回后的操作, 把代码执行的过程, 也称为 CPS 变换**


比如 

```lisp
(+ (call/cc (lambda x : (x 2))) 4)
```

的 call/cc 就可以看做, 在这里, 上面那个求值过程的函数 (+ x y), 已经要返回了,

类似这种感觉:

```js
let f =(x, cont)=>{
  return cont(x)
}

f(4, (x)=>{retrun x+2})
```

cont 就是接下来要做的事情,这样写出 call/cc 是一个自然的事情,

```js

let call_cc = (cb, cont) => {
  return cb(cont)
}

call_cc((cont)=>{return cont(2)},
        (arg)=>{arg+4})
```

作者写的哪个 lisp 的解释器代码我没太 get 到点, 感觉思路还是模拟*注册一个单个参数的**回调**, 在求值的时候 把当前的解释器执行的过程, 作为这个函数的参数传进去 , 并且这个回调用时候的参数,作为这个 call/cc 表达式求值的结果* 这个过程.

```lisp

(define (eval-self-eval-exp exp env cont)
  (display "eval-self-eval-exp\n")
  (cont exp))


(define (eval-call/cc exp env cont)
  (display "eval-call/cc\n")
  (let ((fn (cadr exp))
        (data-cont (continuation cont)))
    (eval-function-call-list `(,fn ,data-cont) env cont)))


(define (eval-continuation-call exp env cont)
  (display "eval-continuation-call\n")
  (eval-exp (car exp) env
            (lambda (data-cont)
              (let ((wrapped-cont (continuation-cont data-cont)))
                (eval-exp (cadr exp) env
                          (lambda (arg)
                            (wrapped-cont arg)))))))

```

思路还是对 call/cc 求值:

1. 先有一个默认的 cont

```lisp
(lambda (arg) (display arg))
```

2. 遇到 call/cc 的时候保存当前的 cont, 对内部的函数进行求值, 这个可以这么高是有原因的, cont 要被调用一定是在这个回调内(这不废话), 要是不被调用可以以这个函数的本身的返回值为返回值, 这样和定义的行为保持一致

``` lisp
(eval-function-call-list `(,fn ,data-cont) env cont)))
```

3. 在函数内部求值的时候, 关键是关注 (cont x) 这种, 调用 continuation 的情况. 发生这种以后,   


先对对剩下的部分完成求值, 

```
 (eval-exp (car exp) env
```


就可以调用 cont 

```
(cont exp)
```

达到一个近似返回的效果

cont就是之前保存好的 cont,

```lisp
(lambda (arg) (wrapped-cont arg))
```

就是把保存的 cont 进行调用, 并且这一步完了不会对接下来的部分求值. 所以这种

```lisp
(call/cc (lambda  (c2) (c2 1)(10)) ) 
```
只会 1 当求值结果而不是 10, 好好品品.

返回之后, 进行继续的求值


这个我不知道该不该算第三种实现方法, 感觉有些情况解决不了, 可能有的得手动改默认 cont, 作者在这里给的例子都比较简单.


## 参考资料

[1]柯里化的前生今世. https://zhuanlan.zhihu.com/p/34060802  --@何幻