class Solution(object):
    def divide(self, dividend, divisor):
        absDividend, absDivisor, ret = abs(dividend), abs(divisor), 0
        while absDividend >= absDivisor:
            tmp, tmpDivisor = 1, abs(divisor)
            while absDividend >= tmpDivisor:
                absDividend -= tmpDivisor
                ret += tmp
                tmpDivisor = tmpDivisor << 1
                tmp = tmp << 1
        if dividend * divisor > 0:
            return min(2147483647,ret)
        else:
            return -ret