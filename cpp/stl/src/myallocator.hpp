//
// Created by 苏畅 on 2019/5/22.

#include <new>
#include <iostream>
#include <cstdio>

# define __THROW_BAD_ALLOC std::cerr <<"out of mem" <<std::endl; exit(1)

// malloc-based allocator

namespace myallo {
    template<int inst>
    class __malloc_alloc_template {
    private:
        // ooom : 用于处理内存不足
        static void *oom_malloc(size_t);

        static void *oom_realloc(void *, size_t);

        static void (*__malloc_alloc_oom_handler)();

    public:
        static void *allocate(size_t n) {
            void *result = malloc(n);
            if (0 == result) result = oom_malloc(n);
            return result;
        }

        static void deallocate(void *p, size_t /*n*/) {
            free(p);
        }

        static void * reallocate(void *p , size_t old_size, size_t new_sz) {
            void * result = realloc(p, new_sz);
            if (0 == result) result = oom_realloc(p, new_sz);
            return result;
        }

        static void (* setm_malloc_handler (void (*f) ()))   () {
                // 函数 接受一个 void() f, 返回一个 *
                void (* old) () = __malloc_alloc_oom_handler;
            __malloc_alloc_oom_handler = f;
            return old;
        };


    };

    template <int inst > //特化 int
    void (* __malloc_alloc_template<inst>::__malloc_alloc_oom_handler) () = 0;

    template <int  inst> //特化 int
    void * __malloc_alloc_template<inst>::oom_malloc(size_t n) {
        void (* my_malloc_handler) ();

        void * result;

        for (;;) {
            my_malloc_handler = __malloc_alloc_oom_handler;
            if (0 == my_malloc_handler) {
                __THROW_BAD_ALLOC;
            }

            (*my_malloc_handler) ();

            result = malloc(n);
            if (result) return (result);
        }

    }

    typedef __malloc_alloc_template<0> malloc_alloc;

}


