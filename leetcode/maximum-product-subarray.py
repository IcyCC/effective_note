class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums :
            return 0
        t_min = nums[0]
        t_max = nums[0]
        res = nums[0]
        for i in nums[1:]:
            if i < 0:
                # 遇到负数反转
                t_max, t_min = t_min, t_max
            t_max = max(i, i*t_max) # 核心思路 要么一直乘过来 要么从i开始乘
            t_min = min(i, i*t_min) # 负数
            res = max (res ,t_max)
        return res