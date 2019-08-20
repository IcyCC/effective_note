class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        fist = float('inf')
        second = float('inf')
        for i in nums:
            if i <= fist:
                fist = i
            elif i <= second:
                second = i
            elif i > second:
                return True
        return False


