from typing import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()

        def slove(s, tmp):
            nonlocal res
            if len(tmp) == 4:
                if not s:
                    res.add('.'.join([str(t) for t in tmp]))
                return
            if not s:
                return
            for i in range(1, 4):
                v_s = s[:i]
                if (not v_s):
                    return
                else:
                    v = int(v_s)
                    if len(v_s) > 1 and v_s.startswith('0'):
                        return
                    if not 0 <= v <= 255:
                        return
                    tmp.append(v)
                    slove(s[i:], list(tmp))
                    tmp.pop()

        slove(s, [])
        return list(res)
