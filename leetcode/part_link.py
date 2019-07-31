# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Divide:
    def listDivide(self, head, val):
        # write code here
        node = head
        lte = ListNode(0)
        gte = ListNode(0)
        lte_head = lte
        gte_head = gte
        while node:
            next_node = node.next
            if node.val <= val:
                lte.next = node
                lte = lte.next
            else:
                gte.next = node
                gte = gte.next
            node.next = None
            node = next_node
        lte.next = gte_head.next
        return lte_head.next
        
                