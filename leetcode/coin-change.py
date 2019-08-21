class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [9999999 for i in range(amount + 1)]
        f[0] = 0
        for i in range(len(f)):
            for c in coins:
                if c <= i:
                    f[i] = min(f[i], f[i - c] + 1)

        return f[-1] if f[-1] < 9999999 else -1