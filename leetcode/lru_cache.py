class LinkNode:

    def __init__(self, key, v):
        self.key = key
        self.v = v
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hash = dict()
        self.link_head = LinkNode(-1, -1)
        self.link_tail = LinkNode(-1, -2)
        self.link_tail.pre = self.link_head
        self.link_head.next = self.link_tail

        self.capacity = capacity
        self.num = 0

    def up(self, node):
        next = self.link_head.next
        if next != node:
            node.pre.next = node.next
            node.next.pre = node.pre
            next.pre = node
            self.link_head.next= node
            node.next = next
            node.pre = self.link_head

    def get(self, key: int) -> int:
        node = self.hash.get(key, None)
        if node:
            self.up(node)
            return node.v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            if self.num < self.capacity:
                self.num = self.num + 1
            else:
                node = self.link_tail.pre
                del self.hash[node.key]
                node.pre.next = self.link_tail
                self.link_tail.pre = node.pre
            node = LinkNode(key, value)
            node.pre = self.link_head
            node.next = self.link_head.next
            node.next.pre = node
            self.link_head.next = node
            self.hash[node.key] = node
        else:
            self.hash[key].v = value
            self.up(self.hash[key])

