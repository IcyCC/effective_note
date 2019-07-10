left_v+right_v+node.val,# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _max = None
        cache = list()
        def get_max(node):
            nonlocal _max
            if not node:
                return 0
            left_v =  get_max(node.left)
            right_v = get_max(node.right)
            #1 要
            res = max(left_v+node.val, right_v+node.val, node.val)
            if _max is None:
                _max = res
            _max = max(left_v+right_v+node.val, res, _max)
            return res

        get_max(root)

        if _max is None:
            return 0
        else:
            return _max

