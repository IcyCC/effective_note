class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        have_set = set()
        _max = 0
        for n in num_set:
            if n not in have_set:
                have_set.add(n)
                v = n + 1
                tmp_max = 1
                while v in num_set:
                    have_set.add(v)
                    v = v + 1
                    tmp_max = tmp_max + 1
                _max = max(_max, tmp_max)
        return _max


