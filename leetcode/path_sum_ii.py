class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(node, p:list, num):
            if not node:
                return
            nonlocal res
            p.append(node.val)
            if num + node.val == sum:
                if (node.right is None) and (node.left is None):
                    res.append(p)
                    return
            num = num + node.val
            dfs(node.left, list(p), num)
            dfs(node.right, list(p), num)
        dfs(root, [], 0)
        return res
