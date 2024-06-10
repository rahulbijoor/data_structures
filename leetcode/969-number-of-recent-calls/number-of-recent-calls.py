class RecentCounter(object):

    def __init__(self):
        self.heap=[]
        heapq.heapify(self.heap)

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        heapq.heappush(self.heap,t)
        while self.heap[0] < t- 3000:
            heapq.heappop(self.heap)
        return len(self.heap)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)