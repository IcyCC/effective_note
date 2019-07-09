# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_q = list()
        right_q = list()
        left_q.append(root.left)
        right_q.append(root.right)
        while left_q and right_q:
            left = left_q.pop(0)
            right = right_q.pop(0)
            if left == right:
                pass
            else:
                if left is None or right is None:
                    return False
                if right.val != left.val:
                    return False
                left_q.append(left.right)
                left_q.append(left.left)

                right_q.append(right.left)
                right_q.append(right.right)

        if (not left_q) and (not right_q):
            return True
        else:
            return False
