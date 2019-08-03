# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def trans(node):
    if not node:
        return None
    right_node = node.right
    node.right = trans(node.left)    
    tail = node # 找到尾巴节点
    while tail.right:
        tail = tail.right
    tail.right = trans(right_node)
    node.left = None
    return node
    

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        trans(root)
