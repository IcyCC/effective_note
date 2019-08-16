class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return 
        count = 0
        for start in range(k):
            if count >= len(nums):
                return 
            slow = start
            if slow >= len(nums):
                slow = slow % len(nums) 
            tmp = nums[slow]
            while True:
                count = count + 1
                quick = slow + k
                quick = quick %len(nums)
                nums[quick],tmp = tmp, nums[quick]
                slow = quick
                slow = slow % len(nums) 
                if slow == start:
                    break
            start = start + 1
