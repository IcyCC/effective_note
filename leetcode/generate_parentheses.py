def push_stk(stk:list, e):
    if e == '(':
        stk.append(e)
        return True
    else:
        if not stk:
            return False
        p = stk.pop()
        if p == '(':
            return True
        else:
            return False

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        res = list()
        def slove(flag, stk:list, tmp:str):
            if flag == n * 2:
                if push_stk(stk, ')'):
                    if not stk:
                        tmp = tmp + ')'
                        res.append(tmp)
                else:
                    return
            else:
                
                stk_l = list(stk)
                if push_stk(stk_l, '('):
                    tmp_l = str(tmp)
                    tmp_l = tmp_l + '('
                    slove(flag+1, stk_l, tmp_l)
                
                stk_r = list(stk)
                if push_stk(stk_r, ')'):
                    tmp_r = str(tmp)
                    tmp_r = tmp_r + ')'
                    slove(tmp_r, stk_r, tmp_r)
                return
        
        slove(1,list(), str())
        return res



