
NUMBER_MAP = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}

SP_MAP= {
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900: "CM"
}

class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        if num in SP_MAP:
            return SP_MAP[num]
        romans = list(NUMBER_MAP.keys())
        romans.sort(reverse=True)

        for r in romans:
            n = num // r
            if n:
                answer =answer + ''.join([NUMBER_MAP[r] for i in range(n)])
                num = num - n * r
            
        return answer