from functools import lru_cache

@lru_cache(10000)
def match_simple(s, p):
    if not p and s:
        return False
    if not s and not p:
        return True
    s_index = 0
    p_index = 0
    p_ch = p[p_index]
    if p_ch == '*':
        p_index = p_index + 1
        while p_index < len(p) and p[p_index] == '*':
            p_index = p_index + 1
        p_index = p_index - 1
        
        while s_index <= len(s):
            res = match_simple(s[s_index:], p[p_index+1:])
            if res == True:
                return True
            s_index = s_index + 1
        return False
    elif p_ch == '?':
        if not s:
            return False
        return match_simple(s[s_index+1:], p[p_index+1:])
    else:
        if not s:
            return False
        if s[s_index] == p_ch:
            return match_simple(s[s_index+1:], p[p_index+1:])
        else:
            return False
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return match_simple(s,p)