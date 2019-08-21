class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        f = [[0 for j in range(n)] for i in range(m)]
        f[0][0] = 1
        for x in range(0, m):
            for y in range(0, n):
                if x > 0:
                    f[x][y] = f[x-1][y] + f[x][y]
                if y > 0:
                     f[x][y] = f[x][y-1] + f[x][y]
        return f[-1][-1]
        