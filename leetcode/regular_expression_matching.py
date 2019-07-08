def match_simple(s, p):
    s_flag = 0
    p_flag = 0
    if not p:
        return not s

    while p_flag < len(p):
        if p_flag + 1 < len(p) and p[p_flag + 1] == '*':
            p_flag = p_flag + 1
            continue
        else:
            if p[p_flag] == '.':
                if s_flag >= len(s):
                    return False
                s_flag = s_flag + 1
            elif p[p_flag] != '*':
                if s_flag >= len(s):
                    return False
                if p[p_flag] != s[s_flag]:
                    return False
                else:
                    s_flag = s_flag + 1
            else:
                pre = p[p_flag - 1]
                while s_flag < len(s) and (s[s_flag] == pre or pre == '.'):
                    res = match_simple(s[s_flag:], p[p_flag + 1:])
                    if res:
                        return True
                    s_flag = s_flag + 1
        p_flag = p_flag + 1
        if p_flag >= len(p):
            if s_flag >= len(s):
                return True
            else:
                return False
    return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return match_simple(s, p)
