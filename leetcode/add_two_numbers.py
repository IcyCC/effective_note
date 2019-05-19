# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_longest_tuple(l1, l2):
    n1 = l1
    n2 = l2
    while True:
        yield (n1, n2)

        if n1.next is None and n2.next is None:
            return

        if n1.next:
            n1 = n1.next
        else:
            n1 = ListNode(0)

        if n2.next:
            n2 = n2.next
        else:
            n2 = ListNode(0)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        up = 0
        res = None
        tmp = None
        for n1, n2 in get_longest_tuple(l1, l2):
            v = n1.val + n2.val
            v = v + up
            up = v // 10
            v = v % 10
            if res is None:
                res = ListNode(v)
                tmp = res
            else:
                tmp.next = ListNode(v)
                tmp = tmp.next
        if up:
            tmp.next = ListNode(up)
        return res


def build_list():
    l1_head = ListNode(5)
    l1 = l1_head

    l2_head = ListNode(5)
    l2 = l2_head

    return l1_head, l2_head
