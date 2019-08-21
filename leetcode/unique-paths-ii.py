class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        f = [[0 for j in range(len(i))] for i in obstacleGrid]
        f[0][0] = 1
        for x in range(len(obstacleGrid)):
            for y in range(len(obstacleGrid[x])):
                if x > 0:
                    f[x][y] = f[x-1][y] + f[x][y]
                if y > 0:
                    f[x][y] = f[x][y-1] + f[x][y]
                if obstacleGrid[x][y] == 1:
                    f[x][y] = 0
        return f[-1][-1]
    