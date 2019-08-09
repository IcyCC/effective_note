class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if not B:
            return 1
        if not A:
            return -1
         # 初始化
        res = 1
        index_a = 0
        index_b = 0
        pre = 0
        while index_b < len(B):
            if B[index_b] not in A:
                return -1
            if index_a >= len(A):
                res = res + 1
                index_a = 0
            if B[index_b] == A[index_a]:
                index_b = index_b + 1
            elif A[index_a] != B[index_b]:
                if pre >= len(A):
                    return -1
                if res > 1:
                    res = res - 1
                index_a = pre
                index_b = 0
                pre = pre  + 1
            index_a = index_a + 1
        return res
            