class SmallestInfiniteSet:

    def __init__(self):
       self.pq=[n for n in range(1,1001)]
       print(self.pq)
       self.popped=set()
       heapq.heapify(self.pq) 

    def popSmallest(self) -> int:
        
        ele = heapq.heappop(self.pq)
        self.popped.add(ele)
        return ele
        
        

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
            heapq.heappush(self.pq, num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)