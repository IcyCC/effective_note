class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}
        if len(s) != len(t):
            return False
            
        for i in s:
            counter_s[i] = counter_s.get(i, 0) + 1
        for i in t:
            counter_t[i] = counter_t.get(i, 0) + 1
        
        for i in set(s+t):
            if counter_s.get(i,0) != counter_t.get(i,0):
                return False
        return True
        