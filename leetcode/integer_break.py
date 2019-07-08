class Solution:
    def integerBreak(self, n: int) -> int:
        cache = [0 for i in range(n+1)]
        cache[0] = 1
        cache[1] = 1
        cache[2] = 1
        def slove(num):
            nonlocal cache
            if cache[num]:
                return cache[num]
            res = [max(slove(num-i) * i, (num-i)*i) for i in range(1, num)]
            cache[num] = max(res)
            return cache[num]
        return slove(n)


class Solution:
    """
      f[x] = max {  
          n * f[x-n],
          n * (x-n)
      }
      // n->(1,x)
    """
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], dp[j]*(i-j), (i-j)*j)
        return dp[n]  