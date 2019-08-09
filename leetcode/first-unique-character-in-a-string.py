class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0) + 1
        for i,c in enumerate(s):
            if counter[c] == 1:
                return i
        
        return -1