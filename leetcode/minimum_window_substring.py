from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        res = ''
        tmp = list()
        t_set = list(t)
        t_counter= Counter(t)
        reqired = sum(t_counter.values())
        has_num = 0
        has = dict()
        while r < len(s):
            ch = s[r]
            if ch in t_counter and has.get(ch, 0) < t_counter[ch]:
                has_num = has_num + 1
            has[ch] = has.get(ch, 0) + 1
            if has_num == reqired:
                while l <= r:
                    ch = s[l]
                    has[ch] = has[ch] - 1
                    if has[ch] < t_counter[ch]:
                        has_num = has_num - 1
                        if res:
                            res = res if len(res) < (r - l + 1) else s[l:r + 1]
                        else:
                            res = s[l:r + 1]
                        l = l + 1
                        break
                    l = l + 1
            r = r + 1
        return res