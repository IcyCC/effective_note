class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = [0 for i in range(len(nums) + 1)]
        pick = 0
        f[1] = nums[0]
        for i in range(2, len(nums)+1):
            idx = i - 1
            v = nums[idx]
            if f[i-2]+ v > f[i-1]:
                # 选取
                f[i] = f[i-2] + v
            else:
                f[i] = f[i-1]
        return f[-1]
