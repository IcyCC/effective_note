# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         f = [9999999 for i in range(amount + 1)]
#         f[0] = 0
#         for i in range(len(f)):
#             for c in coins:
#                 if c <= i:
#                     f[i] = min(f[i], f[i - c] + 1)
#
#         return f[-1] if f[-1] < 9999999 else -1

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
A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
quick_sort(A, 0, len(A) - 1)