# from typing import *
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder_flag = len(postorder)-1
        if postorder:
            def slove(root:TreeNode,left:List[int], right:List[int]):
                nonlocal postorder_flag
                # left
                if right:
                    right_root = TreeNode(postorder[postorder_flag])
                    postorder_flag = postorder_flag - 1
                    root.right = slove(right_root, 
                                       right[:right.index(right_root.val)],
                                       right[right.index(right_root.val)+1:])
                    # left
                if left:
                    left_root = TreeNode(postorder[postorder_flag])
                    postorder_flag = postorder_flag - 1
                    root.left = slove(left_root, 
                                      left[:left.index(left_root.val)], 
                                      left[left.index(left_root.val)+1:])
                return root
            
            root = TreeNode(postorder[postorder_flag])
            postorder_flag = postorder_flag-1
            right = inorder[inorder.index(root.val)+1:]
            left = inorder[:inorder.index(root.val)]
            root = slove(root,left, right)
            return root
        else:
            return None

        

