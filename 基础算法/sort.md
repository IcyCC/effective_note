# 冒泡排序

```python
class BubbleSort:
    def bubbleSort(self, A, n):
        # write code here
        for i in range(n):
            for j in range(n-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A
```

# 选择排序

```python
class SelectionSort:
    def selectionSort(self, A, n):
        # write code here
        for i in range(n):
            for j in range(i+1,n):
                if A[j] < A[i]:
                    A[i], A[j] = A[j], A[i]
        return A
```

# 插入排序

```python
class InsertionSort:
    def insertionSort(self, A, n):
        # write code here
        for i in range(1,n):
            for j in range(0,i):
                if A[i-j] < A[i-j-1]:
                    A[i-j], A[i-j-1] = A[i-j-1], A[i-j]
        return A
```

# 归并

```python
class MergeSort:
    def mergeSort(self, A, n):
        # write code here
        def merge_sort(A):
            l = len(A)
            if l == 1:
                return A
            a = merge_sort(A[:l//2])
            b = merge_sort(A[l//2:])
            res = []
            a_idx = 0
            b_idx = 0
            while a_idx < len(a) and b_idx < len(b):
                if a[a_idx] > b[b_idx]:
                    res.append(b[b_idx])
                    b_idx = b_idx + 1
                else:
                    res.append(a[a_idx])
                    a_idx = a_idx + 1
            res.extend(a[a_idx:])
            res.extend(b[b_idx:])
            return res
        return merge_sort(A)
```

# 快速排序

```python
def partion(A, low, high, povit):
    A[high], A[povit] = A[povit], A[high]
    start = low
    for i in range(low, high):
        if A[i] <= A[high]:
            A[i], A[start] = A[start],A[i]
            start = start + 1
    A[start], A[high] = A[high], A[start]
    return start

def quick_sort(A, low, high):
    if low < high:
        p = partion(A,low, high, (low+high)//2)
        quick_sort(A, low, p-1)
        quick_sort(A, p+1, high)
```
