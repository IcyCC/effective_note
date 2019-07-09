
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def build_bst(start, end, limit_min):
            if start == end:
                return True
            root = preorder[start]
            if root < limit_min:
                return False
            if end - start == 1:
                return True
            for i in range(start+1, end):
                if end < limit_min:
                    return False
                if preorder[i] > root:
                    left = build_bst(start + 1, i, limit_min)
                    limit_min = root
                    right = build_bst(i, end, limit_min)
                    return left and right
            return build_bst(start+1,end, limit_min)

        return build_bst(0,len(preorder), 0)



class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        _stack = []
        limit_min = 0
        for i in preorder:
            if i < limit_min:
                return False
            while(_stack and i > _stack[-1]):
                limit_min = _stack.pop()
            _stack.append(i)
        return True
