# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def slove(r):
            r.left, r.right = r.right, r.right
            slove(r.right)
            slove(r.left)
            return r
        return slove(root)
