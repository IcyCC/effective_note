# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def slove(node, a, b):
    if node is None:
        return None
    if node is a or node is b:
        right = slove(node.right, a, b)    
        left = slove(node.left, a, b)
        return node
    else:
        right = slove(node.right, a, b)    
        left = slove(node.left, a, b)
        if right and left:
            return node
        elif right and not left:
            return right
        elif left and not right:
            return left
        
    

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return slove(root, p, q)
        