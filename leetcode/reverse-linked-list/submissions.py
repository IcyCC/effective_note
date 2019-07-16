# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        _next = None
        while head:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        return pre