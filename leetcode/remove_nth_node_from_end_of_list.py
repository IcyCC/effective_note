from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        link_map = {}
        length = 0
        node = head
        while node:
            length = length + 1
            link_map[length] = node
            node = node.next
        
        r = length - n + 1
        
        if r == 1:
            return link_map[1].next
        elif r == length:
            link_map[r -1].next = None
            return head
        else:
            link_map[r-1].next = link_map[r+1]
            link_map[r].next = None
            return head