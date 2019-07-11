# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def mserialize(node):
            res = 'None'
            if node:
                if node.val is not None:
                    res = str(node.val)
                res = res + ',' + mserialize(node.left)
                res = res + ',' + mserialize(node.right)
            return res
        return mserialize(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def mdeserialize(l):
            if not l:
                return None
            value = l.pop(0)
            if value != 'None':
                node = TreeNode(None)
                node.val = int(value)
                node.left = mdeserialize(l)
                node.right = mdeserialize(l)
                return node
            return None

        return mdeserialize(data.split(','))

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))