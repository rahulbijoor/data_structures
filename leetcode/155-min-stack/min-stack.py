class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.mainStack:
            self.mainStack.append(val)
            self.minStack.append(val)
            return
        minVal = min(val,self.minStack[-1])
        self.mainStack.append(val)
        self.minStack.append(minVal)
        

    def pop(self) -> None:
        if not self.mainStack:
            return
        self.mainStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()