class MinStack:

    def __init__(self):
        self.Stack=[]
        self.minVal=[]

    def push(self, val: int) -> None:
        if len(self.Stack) == 0:
            self.minVal.append(val)
        else:
            self.minVal.append(min(self.minVal[-1],val))
        
        self.Stack.append(val)

        

    def pop(self) -> None:
        self.Stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()