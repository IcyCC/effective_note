class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = [0 for n in nums]
        C = [1 for n in range(len(nums))]
        for idx, v in enumerate(nums):
            f[idx] = 1
            for j in range(1, idx + 1):
                if nums[idx - j] < v:
                    if f[idx - j] >= f[idx]:
                        C[idx] = C[idx - j]
                        f[idx] = f[idx - j] + 1
                    elif f[idx - j] + 1 == f[idx]:
                        C[idx] = C[idx] + C[idx - j]

        res = 0
        _max = max(f)
        for idx, v in enumerate(f):
            if v == _max:
                res = res + C[idx]
        return res

