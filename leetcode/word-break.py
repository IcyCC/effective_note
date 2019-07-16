from typing import *
from functools import lru_cache

#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(1000)
        def slove(s):
            nonlocal wordDict
            buf = []
            if not s:
                return True
            for i in range(len(s)):
                buf.append(s[i])
                if buf in wordDict:
                    flag = slove(s[i + 1:])
                    if flag:
                        return True
            return False

        return slove(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False for i in range(len(s) + 1)]

        f[0] = True

        for i in range(1, len(s) + 1):
            for k in range(1, i+1):
                if s[k-1:i]in wordDict and f[k-1]:
                    f[i] = True
                    break

        return f[len(s)]

print(Solution().wordBreak("leetcode",
["leet","code"]))

