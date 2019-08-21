
class Solution:
    def numDecodings(self, s: str) -> int:
        can_code = ['{}'.format(i) for i in range(1, 27)]
        print(can_code)
        if not s :
            return 0
        f = [0 for i in range(len(s)+1)]
        f[0] = 0
        for d in range(1,len(s)+1):
            if s[:d] in can_code:
                f[d] = 1
            for p in range(1,d):
                if s[p:d] in can_code:
                    f[d] = f[d] + f[p]
        return f[-1]
    