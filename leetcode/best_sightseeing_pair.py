from typing import *

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if A:
            li = [A[i] + i for i in range(len(A))]
            lj = [A[j] - j for j in range(len(A))]

            res = 0
            max_li = li[0]
            for j in range(1, len(A)):
                if max_li + lj[j] > res:
                    res = max_li + lj[j]
                max_li = max(li[j], max_li)
            return res
        else:
            return 0

print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))