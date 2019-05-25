from typing import *

lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = list()
        if not digits:
            return res
        def slove(tmp_res:str, flag, alpha):
            nonlocal res
            tmp_res = tmp_res + alpha
            if flag == len(digits) - 1:
                res.append(tmp_res)
                return
            else:
                next_d = lookup[digits[flag + 1]]
                for a in next_d:
                    slove(str(tmp_res), flag + 1, a)
            return
        for a in  lookup[digits[0]]:
            slove('', 0, a)
        return res
