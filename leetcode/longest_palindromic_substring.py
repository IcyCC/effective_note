
def is_back_str(s1):
    return s1 == s1[::-1]
        

def get_end_poses(s, p, start_pos):
    res= []
    for i in range(start_pos, len(s)):
        if s[i] == p:
            if i >= start_pos:
                res.append(i)
    return res

def slove(s):
    results = []
    res = ''
    for start_pos in range(len(s)):
        end_poss = get_end_poses(s, s[start_pos], start_pos)
        end_poss.reverse()
        for e in end_poss:
            if e - start_pos < len(res):
                break
            if is_back_str(s[start_pos:e+1]):
                results.append(s[start_pos: e+1])
                if len(res) < len(s[start_pos: e+1]):
                    res = s[start_pos: e+1]
    for r in results:
        if len(r) > len(res):
            res = r
    return res



class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = slove(s)
        return r
