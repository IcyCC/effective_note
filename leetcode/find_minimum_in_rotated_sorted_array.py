class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        if r>1:
            mid = (l + r) // 2
            while l < r and nums[l] > nums[r-1]:
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid
            return nums[l] if nums[l] < nums[mid] else nums[mid]
        elif r==1:
            return nums[0]
        else:
            return None