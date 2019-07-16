# Definition for singly-linked list.
            class ListNode:
                def __init__(self, x):
                    self.val = x
                    self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reserve(l1)
        l2 = self.reserve(l2)
        head = ListNode(0)
        res = head
        add_flag = 0

        while l1 is not None or l2 is not None:
            val = add_flag
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            add_flag = 0
            if val >= 10:
                val = val - 10
                add_flag = 1
            head.next = ListNode(val)
            head = head.next
        if add_flag:
            head.next = ListNode(add_flag)
            head = head.next
        return self.reserve(res.next)

    def reserve(self, head):

        pre = None
        _next = None
        while head is not None:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        return pre
