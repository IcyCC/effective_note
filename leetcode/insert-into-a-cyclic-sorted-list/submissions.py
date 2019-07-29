"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not  head:
            node = Node(insertVal, None)
            node.next = node
            return node
        current_node = head
        start_current = head
        next_node = head.next
        if current_node == next_node:
            node = Node(insertVal, None)
            current_node.next = node
            node.next = current_node
            return head
        
        tail = None
        while True:
            if next_node.val >= insertVal and current_node.val <= insertVal:
                # 找到插入位置
                node = Node(insertVal, next_node)
                current_node.next = node
                return head
            if next_node.val <= current_node.val:
                tail = current_node
            next_node = next_node.next
            current_node = current_node.next
            if current_node == start_current:
                if tail is None:
                    # 没找到 说明相同
                    tail = current_node
                node =  Node(insertVal, tail.next)
                tail.next = node
                return head