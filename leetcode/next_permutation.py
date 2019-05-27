from typing import *



def bubble_sort(blist, start):
    count = len(blist)
    for i in range(start, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums) == 1:
            return
        if len(nums) == 2:
            if nums[0] < nums[1]:
                nums[0],nums[1] = nums[1], nums[0]
                return
            nums.sort()
            return
        length = len(nums) - 1
        n = len(nums) - 1
        changed = False
        # 交换
        flag = 0
        while n > 0:
            if nums[n -1] < nums[n]:
                flag = n - 1
                changed = True
                break
            n = n -1
        min_value = nums[flag+1]
        min_flag = flag+1

        if changed:
            n = flag + 1
            while n <= length:
                if nums[n] > nums[flag]:
                    if nums[n] < min_value:
                        min_value = nums[n]
                        min_flag = n
                n = n + 1
            print(flag, min_flag)
            if flag != min_flag:
                nums[flag], nums[min_flag] = nums[min_flag], nums[flag]
                bubble_sort(nums, flag+1)
                return
        else:
            nums.sort()
            return

        


