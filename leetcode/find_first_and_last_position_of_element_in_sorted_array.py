
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) -1
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]
            
        while lo != hi:
            if nums[lo]== nums[hi]:
                break
            
            mid = (lo + hi) //2
            if nums[mid] > target:
                hi = mid
            elif nums[mid]<target:
                lo = mid + 1
            else:
                lo = mid
                hi = mid
                while lo >0 and nums[lo] == nums[lo -1]:
                    lo = lo - 1
                while hi < len(nums) - 1 and nums[hi] == nums[hi + 1]:
                    hi = hi + 1
                
                
        if nums[lo] != target:
            return [-1, -1]
        else:
            return [lo, hi]
