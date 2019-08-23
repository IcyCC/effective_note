# 非递归便利

## 前序

最好想 不多解释

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
          return []
        s = list()
        s.append(root)
        res = []
        while s:
          node = s.pop()
          res.append(node.val)
          if node.right:
            s.append(node.right)
          if node.left:
            s.append(node.left)
        return res


```

## 中序

一个栈 一只压 left, 没了 弹出 记录, 压 right

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s = list()
        cur = root
        res = []
        while cur:
          s.append(cur)
          if cur.left:
            cur = cur.left
          else:
            while s:
              node = s.pop()
              res.append(node.val)
              cur = node.right
              if node.right:
                break

        return res
```

## 后序

按照 根-右-左 遍历 然后反方向

```
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        s1 = list()
        s2 = list()
        res = list()
        if not root:
          return []
        s1.append(root)
        while s1:
          node = s1.pop()
          s2.append(node)
          if node.left:
            s1.append(node.left)
          if node.right:
            s1.append(node.right)

        while s2:
          node = s2.pop()
          res.append(node.val)
        return res
```

## 按层

利用特性 遍历完上一行最右的时候的, next_last 一定是下一行最右的

```
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = Queue()
        last = root
        res = list()
        tmp = list()
        if not root:
          return []
        q.put(root)
        next_last = root
        while not q.empty():
          node = q.get()
          tmp.append(node.val)
          if node.left:
            q.put(node.left)
            next_last = node.left
          if node.right:
            q.put(node.right)
            next_last = node.right
          if node == last:
            # 当前行最后一个节点
            last = next_last
            res.append(list(tmp))
            tmp.clear()
        return res[::-1]
```

## Z 字遍历二叉树

```
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
```
