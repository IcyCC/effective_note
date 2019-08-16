# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        start_head = None
        fix_node = None
        if (not nodeA) or (not nodeB):
            return None
        if nodeA is nodeB:
            return nodeA
        while nodeA.next and nodeB.next:
            nodeA = nodeA.next
            nodeB = nodeB.next
        if nodeA.next is None:
            while nodeB.next:
                nodeB = nodeB.next
            nodeB.next = headA
            fix_node = nodeB
            start_head = headB
        else:
            while nodeA.next:
                nodeA = nodeA.next
            nodeA.next = headB
            fix_node = nodeA
            start_head = headA
        slow = start_head
        fast = start_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = start_head
                while True:
                    slow = slow.next
                    fast = fast.next
                    if slow is fast:
                        fix_node.next = None
                        return slow

        fix_node.next = None

        return None
            