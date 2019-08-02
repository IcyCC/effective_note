"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (not head):
            return head
        node = head
        node = head
        while node:
            next_node  = node.next
            node.next = Node(node.val, next_node, None)
            node = next_node
        copy_head = None
        node = head
        while node:
            copy_node = node.next # 找到复制的节点
            next_node = node.next.next
            if node.random:
                copy_node.random = node.random.next
            node = next_node
        node = head
        while node:
            copy_node = node.next # 找到复制的节点
            if not copy_head:
                copy_head = copy_node
            next_node = copy_node.next
            node.next = next_node
            if copy_node.next:
                copy_node.next = next_node.next
            node = next_node
        # copy_node = copy_head
        # while copy_node:
        #     print(id(copy_node))
        #     copy_node = copy_node.next
        return copy_head            
