
def slove(s, l, f):
    if l == 0:
        f.append(1)
        return 1
    else:
        res = slove(s, l-1, f)
        p = s[l-res:l].rfind(s[l]) + l-res
        if p != -1:
            f.append(l-p)
            return l - p
        else:
            f.append(res+1)
            return res + 1
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            f = list()
            slove(s, len(s)-1, f)
            return max(f)
        else:
            return 0