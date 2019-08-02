# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def get_link_mid(node):
    slow = node
    quick = node
    while quick and quick.next:
        quick = quick.next.next
        slow = slow.next
    return slow


def reserve_link_list(head):
    pre = None
    node = head
    while node:
        node_next = node.next
        node.next = pre
        pre = node
        node = node_next
    return pre

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        mid_node = get_link_mid(head)
        mid_node_next = mid_node.next
        mid_node.next = None
        mid_node = reserve_link_list(mid_node_next)
        node = head
        while mid_node:
            node_next = node.next
            mid_node_next = mid_node.next
            node.next = mid_node
            mid_node.next = node_next
            mid_node = mid_node_next
            node = node_next
        
        
        