class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for j in range(N+1)] for i in range(K+1)]
        for step in range(1, N+1):
            dp[0][step] = 0
            for k in range(1,K+1):
                dp[k][step] = dp[k-1][step-1] + dp[k][step-1] + 1
                if dp[k][step] >= N:
                    return step
        return N
                
            
            
        
        