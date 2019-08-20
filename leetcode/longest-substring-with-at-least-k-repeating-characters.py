from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def slove(s):
            c = Counter(s)
            for idx, v in enumerate(s):
                if c[v] < k:
                    return max(slove(s[:idx]), slove(s[idx + 1:]))
            return len(s)

        return slove(s)

