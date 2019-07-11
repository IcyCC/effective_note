from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        res = 0
        while i < len(height)-1:
            if height[i] > 0:
                max_value = (0, i)
                break_flag = False
                for j in range(i + 1, len(height)):
                    if height[j] > height[i]:
                        # 大 计算面积
                        for n in height[i + 1:j]:
                            res = res + (height[i] - n)
                        i = j
                        break_flag = True
                        break
                    max_value = (max_value[0], max_value[1]) if max_value[0] > height[j] else (height[j], j)
                if not break_flag:
                    # 没找到
                    for n in height[i + 1:max_value[1]]:
                        res = res + (max_value[0] - n)
                    i = max_value[1]
            else:
                i = i +1

        return res

print(
Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
)


