# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        res = set()
        if node:
            while node.next is not None:
                if node in res:
                    return node
                else:
                    res.add(node)
                    node = node.next
        return None