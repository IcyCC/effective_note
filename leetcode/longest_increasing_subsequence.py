class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = list([1 for i in range(len(nums) + 1)])
        dp[1] = 1
        dp[0] = 0
        for i in range(2, len(nums) + 1):
            v = nums[i - 1]
            for n in range(1,i):
                if nums[n-1] < v and dp[n] >= dp[i]:
                    dp[i] = dp[n] + 1
        return max(dp)