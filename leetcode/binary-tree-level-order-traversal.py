# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = list()
        current_num = 0
        next_num = 0
        q.append(root)
        current_num = current_num + 1
        res=list()
        tmp = list()
        while q:
            node = q.pop(0)
            current_num = current_num -1
            if node is not None:
                tmp.append(node.val)
                q.append(node.left)
                q.append(node.right)
                next_num = next_num + 2
            if current_num == 0:
                if tmp:
                    res.append(list(tmp))
                tmp.clear()
                current_num = next_num
                next_num = 0
        return res