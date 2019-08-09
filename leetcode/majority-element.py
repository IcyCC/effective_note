class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        res = nums[0]
        for i in nums[1:]:
            if res != i:
                counter = counter - 1
            else:
                counter = counter + 1
            if counter == 0:
                res = i
                counter = 1
        return res