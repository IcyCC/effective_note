class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start_head = ListNode(0)
        start_head.next = head
        start = None
        flag = 0
        if m == n:
            return head
        while head is not None:
            flag = flag + 1
            if flag == m - 1:
                start = head
            if flag == m:
                s = self.reverseList(head, n - m)
                if start:
                    start.next = s
                if m == 1:
                    start_head.next = s
                break
            head = head.next
        return start_head.next

    def reverseList(self, head: ListNode, n) -> ListNode:
        if not head:
            return head
        pre = None
        _next = None
        end = head
        flag = 0
        if n == 0:
            return head
        while head is not None and flag <= n:
            if flag <= n:
                _next = head.next
                head.next = pre
                pre = head
                head = _next
            flag = flag + 1
        end.next = head
        return pre