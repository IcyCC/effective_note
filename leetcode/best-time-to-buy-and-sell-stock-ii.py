
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        hold = False
        for p in range(len(prices)-1):
            if prices[p] < prices[p+1] and not hold:
                # 买入
                res = res - prices[p]
                hold = True
            elif prices[p] > prices[p+1] and hold:
                res = res + prices[p]
                hold = False
        
        if hold:
            res = res + prices[p+1]
                
        return res