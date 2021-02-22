class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> None:
        self.l = self.l[0:-1]

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        ans = self.l[0]
        for i in self.l:
            if i < ans:
                ans = i
        return ans

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
