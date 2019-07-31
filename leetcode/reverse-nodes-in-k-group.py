# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        _stack = list()
        node = head
        if k == 0 or k == 1:
            return head
        tmp_head = None
        pre_tail = None
        while node is not None:
            _stack.append(node)
            node  = node.next
            if len(_stack) == k:
                # 满足全部弹出逆序
                tmp = _stack.pop()
                pre_head = tmp
                if not  tmp_head:
                    tmp_head = tmp
                while _stack:
                    n = _stack.pop()
                    tmp.next  = n
                    tmp = tmp.next
                if pre_tail:
                    pre_tail.next = pre_head
                tmp.next = node
                pre_tail = tmp
        if tmp_head:
            return tmp_head
        else:
            return head