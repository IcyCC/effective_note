//
// Created by 苏畅 on 2019/5/26.
//

#ifndef STL_STL_ITERATOR_HPP
#define STL_STL_ITERATOR_HPP

#include <cstddef>

namespace alloc {
    struct input_iterator_tag {
    }; // 只读迭代器
    struct output_iterator_tag {
    }; // 只写
    struct forward_iterator_tag : public input_iterator_tag {
    }; // 读写
    struct bidirectional_iterator_tag : public forward_iterator_tag {
    }; //双向移动
    struct random_accesss_iterator_tag : public bidirectional_iterator_tag {
    }; //随机读写

    template<class Category, class T, class Distance = ptrdiff_t,
            class Pointer = T *, class Reference = T &>
    struct iterator {
        typedef Category iterator_category; // 定义迭代器的类型
        typedef T value_type;
        typedef Distance difference_type;
        typedef Pointer pointer;
        typedef Reference reference;
    };

    // traits
    template<class Iterator>
    struct iterator_traits {
        typedef typename Iterator::iterator_category iterator_category;
        typedef typename Iterator::value_type value_type;
        typedef typename Iterator::difference_type difference_type;
        typedef typename Iterator::pointer pointer;
        typedef typename Iterator::reference reference;

    };

    template<class T>
    struct iterator_traits<T *> {
        typedef random_accesss_iterator_tag iterator_category;
        typedef T value_type;
        typedef ptrdiff_t difference_type;
        typedef T *pointer;
        typedef T &reference;
    };

    template<class T>
    struct iterator_traits<const T *> {
        typedef random_accesss_iterator_tag iterator_category;
        typedef T value_type;
        typedef ptrdiff_t difference_type;
        typedef T *pointer;
        typedef T &reference;
    };

    template<class Iterator>
    inline typename iterator_traits<Iterator>::iterator_category itemrator_category(const Iterator &) {
        typedef typename iterator_traits<Iterator>::iterator_category category;
        return category();
    }

    template<class Iterator>
    inline typename iterator_traits<Iterator>::difference_type *distance_type(const Iterator &) {
        typedef typename iterator_traits<Iterator>::iterator_category category;
        return static_cast<typename iterator_traits<Iterator>::difference_type *>(0);
    }

    template<class Iterator>
    inline typename iterator_traits<Iterator>::value_type *value_type(const Iterator &) {
        typedef typename iterator_traits<Iterator>::iterator_category category;
        return static_cast<typename iterator_traits<Iterator>::value_type *>(0);
    }


    // 利用函数重载
    // 获取距离 只读迭代器
    template<class InputIterator>
    inline typename iterator_traits<InputIterator>::difference_type
    _distance(InputIterator fist, InputIterator last, input_iterator_tag) {
        typename iterator_traits<InputIterator>::difference_type n = 0;
        while (fist != last) {
            ++fist;
            ++n;
        }
        return n;
    }

    // 随机读取迭代器
    template<class RandonAccessIterator>
    inline typename iterator_traits<RandonAccessIterator>::difference_type
    _distance(RandonAccessIterator fist, RandonAccessIterator last, random_accesss_iterator_tag) {
        return last - fist;
    }

    //暴露给外部的接口
    template<class InputIteraotr>
    inline typename iterator_traits<InputIteraotr>::difference_type distance(InputIteraotr first, InputIteraotr last) {
        typedef typename iterator_traits<InputIteraotr>::iterator_category category;
        return _distance(first, last, category());
    }

    // 1. 指针 用法例子
    template <class T, class Alloc>
    class vector {
    public:
        typedef T  value_type;
        typedef value_type* iterator; // 传入的iterator 使用 T* 来萃取特性
    };
    // 使用vector::iterator

    template <class  T>
    struct __list_node {};

    //2. 复杂例子
    template <class T>
    struct __list_iterator
    {
        typedef bidirectional_iterator_tag iterator_category;
        typedef T value_type;
        typedef ptrdiff_t difference_type;
        typedef T* pointer;
        typedef T& reference;

        typedef __list_node<T>* nodePtr;
        typedef __list_iterator<T> self;

        nodePtr p;

        __list_iterator(const nodePtr& _p = 0):p(_p){}
        bool operator==(const __list_iterator<T>& iter)
        {
            return p==iter.p;
        }
        bool operator!=(const __list_iterator<T>& iter)
        {
            return p!=iter.p;
        }
        reference operator*()const
        {
            return (*p).data;
        }
        pointer operator->()const
        {
            return &((*p).data);
        }

        self& operator++()
        {
            p = (nodePtr)(p->next);
            return *this;
        }

        self operator++(int)
        {
            self tmp = *this;
            p = (nodePtr)(p->next);
            return tmp;
        }

        self& operator--()
        {
            p = (nodePtr)(p->prev);
            return *this;
        }

        self operator--(int)
        {
            self tmp = *this;
            p = (nodePtr)(p->prev);
            return tmp;
        }

    };





}

#endif //STL_STL_ITERATOR_HPP
