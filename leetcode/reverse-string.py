class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 1:
            return 
        l = 0
        h = len(s) -1
        while l <h:
            s[l],s[h] = s[h], s[l]
            l  = l + 1
            h = h -1