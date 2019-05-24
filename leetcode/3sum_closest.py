from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        min_gap = None
        min_sum = None
        for flag in range(len(nums)):
            left = flag + 1
            right = len(nums) - 1

            while left < right:
                r = nums[left] + nums[flag] + nums[right]
                v = r - target
                if min_gap is None:
                    min_gap = abs(target-r)
                    min_sum = r
                    if v > 0:
                        right = right - 1
                    elif v<0:
                        left = left + 1
                    elif v == 0:
                        break
                else:
                    if min_gap > abs(v):
                        min_gap = abs(v)
                        min_sum = r
                    if v > 0:
                        right = right - 1
                    elif v<0:
                        left = left + 1
                    elif v == 0:
                        break
        return min_sum