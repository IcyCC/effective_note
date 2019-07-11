class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = [1 for i in ratings]
        r = [1 for i in ratings]
        res = 0
        for i in range(1, len(ratings)):
            l[i] = 1 if ratings[i] <= ratings[i - 1] else l[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            r[i] = 1 if ratings[i] <= ratings[i + 1] else r[i + 1] + 1
        t = []
        for i in zip(l, r):
            res = res + max(i[0], i[1])
            t.append(max(i[0], i[1]))
        return res

