class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ''
        res = [list() for  i in range(numRows)]
        pos_p = list( [i for i in range(numRows - 1)])
        pos_p.append(numRows - 1)
        t  = list([i for i in range(1, numRows - 1)])
        t.reverse()
        pos_p.extend(t)
        print(pos_p)
        for i, a in enumerate(s):
            r = i % len(pos_p)
            print("R",r,pos_p[r])
            res[pos_p[r]].append(a)
        for i in res:
            answer = answer + ''.join(i)
        return answer