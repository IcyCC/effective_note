class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_func = {
        '*':  lambda a,b:  a*b,
        '-': lambda a,b:  a-b,
        '+':lambda a,b:  a+b,
        '/':lambda a,b:  int(a/b),
        }
        stack = list()
        for t in tokens:
            if t in op_func.keys():
                b  = stack.pop()
                a = stack.pop()
                res = op_func[t](a,b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]