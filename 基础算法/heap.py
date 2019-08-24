from functools import cmp_to_key
import random


class Headq:
    def __init__(self, max_size=-1, key=None, revser=False):
        if key is None:
            def key(item): return item
        self._key = key
        self._data = []
        self._max_size = max_size
        self._op = 1
        if revser:
            self._op = 0

        self._op_table = (lambda a, b: self._key(a) > self._key(
            b), lambda a, b: self._key(a) < self._key(b))

    @staticmethod
    def _get_left(i):
        return 2 * i + 1

    @staticmethod
    def _get_right(i):
        return 2 * i + 2

    @staticmethod
    def _get_parent(i):
        return (i - 1) // 2

    def _percolate_up(self, i):

        while self._get_parent(i) >= 0:
            parent = self._get_parent(i)
            if self._op_table[self._op](self._data[parent], self._data[i]):
                break
            else:
                # 交换位置
                self._data[parent], self._data[i] = self._data[i], self._data[parent]
                i = parent
        return i

    def _percolate_down(self, i):
        while self._get_left(i) < len(self._data):
            left_idx = self._get_left(i)
            swap_idx = left_idx
            # 有左孩子
            if not self._get_right(i) >= len(self._data):
                right_idx = self._get_right(i)
                if self._op_table[self._op](self._data[right_idx], self._data[left_idx]):
                    swap_idx = right_idx

            if self._op_table[self._op](self._data[swap_idx], self._data[i]):
                self._data[swap_idx], self._data[i] = self._data[i], self._data[swap_idx]
                i = swap_idx
            else:
                break
        return i

    def push(self, e):
        if self._max_size != -1:
            if len(self._data) >= self._max_size:
                self.pop()
        self._data.append(e)
        self._percolate_up(len(self._data) - 1)

    def pop(self):
        e = self.top()
        self._data[0], self._data[len(
            self._data) - 1] = self._data[len(self._data) - 1], self._data[0]
        self._data.pop()
        self._percolate_down(0)
        return e

    def top(self):
        return self._data[0]

    def heapfiy(self, data):
        """
        直接根据data建立堆
        :param data:
        :return:
        """
        self._data = data[:]
        for i in range(len(self._data)-1, -1, -1):
            self._percolate_down(i)

# 测试 1
h = Headq()


l = [random.randint(1, 100) for j in range(10)]

print(l)

for i in l:
    h.push(i)

res = []
for j in l:
    res.append(h.pop())
print(res)


h.heapfiy(l)
res = []
for j in l:
    res.append(h.pop())
print(res)