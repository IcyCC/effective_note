class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
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
        return Trues