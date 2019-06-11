from typing import *

nums = list([ str(i) for i in range(1 ,10)])

grid = [(0,0), (0, 3), (0, 6),
         (3,0), (3, 3), (3,6),
         (6,0), (6,3), (6,6)]
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #检查每一行
        for i in range(0, 9):
            line = board[i]
            for n in nums:
                if line.count(n) > 1:
                    return False
            
        for i in range(0 , 9):
            line = list()
            for j in range(0,9):
                line.append(board[j][i])
            for n in nums:
                if line.count(n) > 1:
                    return False
        
        for g in grid:
            line = list()
            for i in range(g[0], g[0] + 3):
                line.extend(board[i][g[1]:g[1] +3])
            for n in nums:
                if line.count(n) > 1:
                    return False
        return True