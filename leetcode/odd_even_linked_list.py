# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        i = 1
        pre_node = head
        node = head.next
        tail = head
        length = 0
        while True:
            length = length + 1
            if tail.next:
                tail = tail.next
            else:
                break

        print(length)
        while i < length:
            if (i + 1) % 2 :
                # 奇数
                node = node.next
                pre_node = pre_node.next
            else:
                # 偶数
                pre_node.next  =  node.next
                tail.next = node
                node.next = None
                tail = tail.next
                node = pre_node.next
            i = i + 1
        return head
                