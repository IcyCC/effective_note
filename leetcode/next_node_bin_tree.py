class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            r = pNode.right
            while r.left:
                r = r.left
            return r
                
        else:
            while pNode.next is not None:
                p = pNode.next
                if p.left == pNode:
                    return p
                pNode = pNode.next
            return None