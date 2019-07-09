class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pop_flag = 0
        stack = list()
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[pop_flag]:
                stack.pop()
                pop_flag = pop_flag + 1
                if not pop_flag < len(popped):
                    break

        if pop_flag == len(pop_flag):
            return True
        else:
            return False
