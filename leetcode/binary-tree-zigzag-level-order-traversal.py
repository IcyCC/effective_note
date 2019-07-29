# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        stacks = [list(), list()]
        current_stack = 0
        next_stack = 1
        stacks[current_stack].append(root)
        tmp = list()
        res = list()
        while stacks[current_stack]:
            node = stacks[current_stack].pop()
            if node:
                tmp.append(node.val)
                if next_stack == 1:
                    stacks[next_stack].append(node.left)
                    stacks[next_stack].append(node.right)
                else:
                    stacks[next_stack].append(node.right)
                    stacks[next_stack].append(node.left)
            if not stacks[current_stack]:
                # 为空反转
                if tmp:
                    res.append(list(tmp))
                    tmp.clear()
                current_stack, next_stack = next_stack, current_stack
        return res
                
                