


class Solution:
    def calculate(self, s: str) -> int:
        op_order = {
                '*': 4,
                "/": 4,
                '+' : 1,
                '-': 1
                }

        op_func = {
        '*':  lambda a,b:  a*b,
        '-': lambda a,b:  a-b,
        '+':lambda a,b:  a+b,
        '/':lambda a,b:  a//b,
        }
        if not s:
            return 0
        num_stack = list()
        op_stack = list()
        pos = 0
        res = 0
        while pos<len(s):
            if s[pos] in op_order.keys():
                if not op_stack or op_order[op_stack[-1]] < op_order[s[pos]]:
                    op_stack.append(s[pos])
                else:
                    while op_stack and op_order[op_stack[-1]] >= op_order[s[pos]]:
                        op = op_stack.pop()
                        b = num_stack.pop()
                        a = num_stack.pop()
                        num_stack.append(op_func[op](a,b))
                    op_stack.append(s[pos])
                pos = pos +1
                continue
            else:
                tmp = ''
                while pos < len(s) and  s[pos] not in op_order.keys():
                    tmp = tmp + s[pos]
                    pos = pos + 1
                num_stack.append(int(tmp.strip()))
        while op_stack:
            op = op_stack.pop()
            b = num_stack.pop()
            a= num_stack.pop()
            r = op_func[op](a,b)
            num_stack.append(op_func[op](a,b))
            
        return num_stack[-1]
            
            
                
         