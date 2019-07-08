# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        r_node = ListNode(head.val)
        next_node = head.next
        while next_node:
            node = ListNode(next_node.val)
            node.next=r_node
            r_node = node
            next_node = next_node.next
        return r_node