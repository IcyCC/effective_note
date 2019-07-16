from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def slove(s, tmp):
            if not s:
                res.append(tmp)
                return
            for i in range(1,len(s)+1):
                if self.isPalindrome(s[:i]):
                    slove(s[i:], [*tmp, s[:i]])

        slove(s, list())
        return res


    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not (s[l].isdigit() or s[l].isalpha()):
                l = l + 1
                continue
            if not (s[r].isdigit() or s[r].isalpha()):
                r = r - 1
                continue
            if (r > l):
                if s[l].upper() != s[r].upper():
                    return False
                else:
                    l = l + 1
                    r = r - 1
        return True

print(Solution().partition("aab"))