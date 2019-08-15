class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = list()
        res = []
        for i, v in enumerate(nums):
            start = i - k + 1
            while  q:
                if nums[q[-1]] <= v:
                    q.pop()
                else:
                    break
            q.append(i)
            if start >= 0:
                while q:
                    idx = q[0]
                    if idx >= start:
                        res.append(nums[idx])
                        break
                    else:
                        q.pop(0)
        return res
                    
        
            
            
            