import typing
def slove(start, end, height):
    max_v = 0
    while start < end:
        max_v = max(max_v, min(height[start], height[end]) * (end-start) )
        print(max_v)
        if height[start] <  height[end]:
            start  = start +1
        else:
            end = end - 1
    return max_v
        
        

class Solution:
    def maxArea(self, height: typing.List[int]) -> int:
       
        return slove(0, len(height) -1 , height)
