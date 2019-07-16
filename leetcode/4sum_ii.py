
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter_ab = {}
        res = 0
        for a in A:
            for b in B:
                counter_ab[a+b] = counter_ab.get(a+b, 0)  + 1

        counter_cd = {}
        for c in C:
            for d in D:
                counter_cd[c+d] = counter_cd.get(c+d, 0)  + 1

        for k1 in counter_ab.keys():
            if (0-k1) in counter_cd.keys():
                res = res + counter_ab[k1] * counter_cd[0-k1]
        return res
