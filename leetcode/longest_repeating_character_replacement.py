class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        l = 0
        r = 1
        tmp_counter = {}
        tmp_counter[s[l]] = 1
        max_ch = (s[l], 1)
        tmp_total = 1
        res = 1

        def get_max_item(data):
            _max = None
            for k in data.keys():
                if not _max:
                    _max = (k,data[k])
                else:
                    _max = _max if _max[1] > data[k] else (k,data[k])
            return _max

        while r < len(s):
            if tmp_total - max_ch[1] >= k:
                while r < len(s) and s[r] == max_ch[0] :
                    tmp_counter[s[r]] = tmp_counter[s[r]] + 1
                    tmp_total = tmp_total + 1
                    max_ch = (max_ch[0], max_ch[1] + 1)
                    r = r + 1
                # 不能换了
                res = max(r - l, res)
                while tmp_total - max_ch[1] >= k and l < r:
                    tmp_counter[s[l]] = tmp_counter[s[l]] - 1
                    max_ch = get_max_item(tmp_counter)
                    tmp_total = tmp_total - 1
                    l = l + 1
                if l > r:
                    r = l
            if r < len(s):
                tmp_counter[s[r]] = tmp_counter.get(s[r], 0) + 1
                if tmp_counter[s[r]] > max_ch[1]:
                    max_ch = (s[r], tmp_counter[s[r]])
                tmp_total = tmp_total + 1
                r = r + 1
        return max(res, r - l)


print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("AABABBA", 1))

print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABA", 0))
print(Solution().characterReplacement("AABBBBB", 0))

print(Solution().characterReplacement("AAAA", 0))
print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))


