# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def in_order_travel(root):
    if root.left:
        yield in_order_travel(root.left)
    yield root
    if root.right:
        yield in_order_travel(root.right)
        
        

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        g = in_order_travel(root)
        for i in range(k):
            next(g)
        return n.val