class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        for flag in range(m+n-1, -1, -1):
            if i < 0:
                nums1[flag] = nums2[j]
                j = j - 1
            elif j <0:
                nums1[flag] = nums1[i]
                i = i -1
            else:
                if nums1[i] > nums2[j]:
                    nums1[flag] = nums1[i]
                    i = i - 1
                else:
                    nums1[flag] = nums2[j]
                    j = j -1
            
            
        