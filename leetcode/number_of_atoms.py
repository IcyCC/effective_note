    from typing import *
    from collections import defaultdict


    def pop_unitl_empty(s):
        res = []
        while s:
            res.append(s.pop())
        res.reverse()
        return ''.join(res)


    class Solution:
        def countOfAtoms(self, formula: str) -> str:
            _symbol_stack = []
            _atom_stack = []
            count = defaultdict(lambda: 0)

            def slove(s: str, base):
                print(s, base)
                nonlocal count
                nonlocal _atom_stack
                nonlocal _symbol_stack
                i = 0
                while i < len(s):
                    if s[i] == '(':
                        if not _symbol_stack:
                            f = pop_unitl_empty(_atom_stack)
                            if f:
                                count[f] = count[f] + base
                        _symbol_stack.append(s[i])
                        _atom_stack.append(s[i])
                        i = i + 1
                    elif s[i] == ')':
                        _symbol_stack.pop()
                        if not _symbol_stack:
                            num = 1
                            num_s = ''
                            i = i + 1
                            while i < len(s) and s[i].isdigit():
                                num_s = num_s + s[i]
                                i = i + 1
                            if num_s:
                                num = int(num_s)
                            f = pop_unitl_empty(_atom_stack)
                            slove(f[1:], num * base)
                        else:
                            _atom_stack.append(s[i])
                            i = i + 1
                    else:
                        if s[i].isupper():
                            if _atom_stack and (not _symbol_stack):
                                f = pop_unitl_empty(_atom_stack)
                                if f:
                                    count[f] = count[f] + base
                            _atom_stack.append(s[i])
                            i = i + 1

                        elif s[i].isdigit():
                            if _symbol_stack:
                                _atom_stack.append(s[i])
                                i = i + 1
                            else:
                                num = 1
                                num_s = s[i]
                                i = i + 1
                                while i < len(s) and s[i].isdigit():
                                    num_s = num_s + s[i]
                                    i = i + 1
                                if num_s:
                                    num = int(num_s)
                                f = pop_unitl_empty(_atom_stack)
                                if f:
                                    count[f] = count[f] + base * num
                        else:
                            _atom_stack.append(s[i])
                            i = i + 1
                if _atom_stack:
                    f = pop_unitl_empty(_atom_stack)
                    if f:
                        count[f] = count[f] + base

            slove(formula, 1)
            print(count)

            result = [atom_name + ("" if count[atom_name] == 1 else str(count[atom_name])) for atom_name in
                      count.keys()]
            result.sort()
            return "".join(result)


print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
