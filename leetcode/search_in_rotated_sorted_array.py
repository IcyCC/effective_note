def binary_search(lis, num):
    left = 0
    right = len(lis) - 1
    while left <= right: 
        mid = (left + right) // 2 
        if num < lis[mid]: 
            right = mid - 1  
        elif num > lis[mid]: 
            left = mid + 1 
        else:
            return mid 
    return -1 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        lo, hi = 0, len(nums) -1
        
        def search(l, h):
            nonlocal nums
            nonlocal target
            if l == h:
                return -1
            if nums[l] == target:
                return l
            if nums[h] == target:
                return h
            povit = (h + l) // 2
            if nums[povit] == target:
                return povit
            if nums[povit] < nums[l]:
                # 右半区
                p = binary_search(nums[povit:h+1], target)
                if p != -1:
                    return povit+p
                else:
                    if povit == h:
                        return -1
                    return search(l,povit)
                
            elif nums[povit] > nums[hi]:
                # 左半区
                p = binary_search(nums[l:povit+1], target)
                if p != -1:
                    return l+p
                else:
                    if povit == l:
                        return -1
                    return search(povit,h)
            else:
                p  = binary_search(nums[l:h+1], target)
                if p == -1:
                    return -1
                return  p + l
        
        return search(lo,hi)