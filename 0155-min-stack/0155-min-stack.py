class MinStack:

    def __init__(self):
        self.stack=[]
        self.mistack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mistack)==0 or val<=self.getMin():
            self.mistack.append(val)

    def pop(self) -> None:
        val=self.stack.pop()
        if val==self.getMin():
            self.mistack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mistack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()