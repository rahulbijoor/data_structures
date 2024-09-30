class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[-1]*maxSize
        self.capacity = maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != self.capacity - 1:
            self.top += 1
            self.stack[self.top] = x
        

    def pop(self) -> int:
        if self.top == -1:
            return -1

        ele = self.stack[self.top]
        self.top -= 1
        return ele 

    def increment(self, k: int, val: int) -> None:
        if k > self.capacity:
            k = self.top+1
        for i in range(k):
            self.stack[i] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)