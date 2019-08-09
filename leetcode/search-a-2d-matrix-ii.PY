class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        def search(row_end, cow_start):
            nonlocal matrix
            nonlocal target
            if cow_start == len(matrix):
                return False
            l = 0
            h = row_end
            while l < h:
                print(l, h)
                mid = (l+h)//2
                if matrix[cow_start][mid] < target:
                    l = mid + 1
                elif matrix[cow_start][mid] > target:
                    h = mid
                else:
                    return True
            return search(h, cow_start + 1)
        return search(len(matrix[0]), 0)