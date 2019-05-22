class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for flag in range(len(nums)):  
            if flag != 0 and nums[flag-1]  == nums[flag]:
                continue
            left = flag + 1
            right = len(nums) - 1
            
            while left<right:
                
                pre_left = left
                pre_right =right

                r = nums[left] + nums[flag] + nums[right]
                if r == 0:
                    r =  [nums[left], nums[flag], nums[right]]
                    res.append(r)
                    while  left <right and nums[pre_left] == nums[left]:
                        left = left + 1                
                elif r > 0:
                    while  left <right and nums[pre_right] == nums[right]:                    
                        right = right - 1
                elif r < 0 :
                    while  left <right and nums[pre_left] == nums[left]:
                        left = left + 1
        
        return res