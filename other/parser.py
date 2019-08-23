# E -> E + T
#    | T
# T -> T * F
#    | F
# F -> num

tokens = [('1', 'num'), ('+','add'), ('2', 'num'),('*','puls'), ('5','num')]
flag = 0
def parser_F():
    global flag
    if tokens[flag][1] == 'num':
        v = int(tokens[flag][0])
        flag = flag + 1
        return v
    else:
        raise Exception("F")


def parser_T():
    global flag
    res = parser_F()
    token = tokens[flag]
    while token[0] =='*':
        flag = flag + 1
        res = res * parser_F()
        if flag >= len(tokens):
            break
        token = tokens[flag]
    return res


def pareser_E():
    global flag
    res = parser_T()
    token = tokens[flag]
    while token[0] =='+':
        flag = flag + 1
        if flag >= len(tokens):
            break
        res = res + parser_T()
        token = tokens[flag]
    return res

print(pareser_E())