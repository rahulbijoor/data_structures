class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq1 = []
        pq2 = []
        i=0
        j=len(costs)-1
        heapq.heapify(pq1)
        heapq.heapify(pq2)
        it = k
        ans = 0
        while it > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1
            t1 = 2**64
            t2 = 2**64 
            if len(pq1) > 0:
                t1 =  heapq.heappop(pq1)
            if len(pq2) > 0:
                t2 = heapq.heappop(pq2)
            if t1 <= t2:
                ans += t1
                heapq.heappush(pq2,t2)
            else:
                ans += t2
                heapq.heappush(pq1,t1)
            it -= 1
        return ans
            


