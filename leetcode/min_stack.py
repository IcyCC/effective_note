class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self._s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._s.append(x)
        self.min = min(self._s)

    def pop(self):
        """
        :rtype: None
        """
        self._s.pop(-1)
        if self._s:
            self.min = min(self._s)
        else:
            self.min = None

    def top(self):
        """
        :rtype: int
        """
        return self._s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()