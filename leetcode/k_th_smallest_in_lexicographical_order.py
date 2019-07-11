
class TireNode:

    def __init__(self, v):
        self.val = v
        self.nodes = []


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        root = TireNode('')
        _order = 0
        exit = False
        res = 0
        def build_tire(parent):
            nonlocal _order
            nonlocal res
            nonlocal exit
            if exit:
                return
            for i in range(0, 10):
                if exit:
                    return
                if (not parent.val) and i == 0:
                    continue
                node = TireNode(parent.val + str(i))

                if int(node.val) > n:
                    return
                else:
                    _order = _order + 1
                    root.nodes.append(node)
                    if _order == k:
                        res =  int(node.val)
                        exit = True
                    else:
                        build_tire(node)
        build_tire(root)
        return res

Solution().findKthNumber(4289384,1922239)