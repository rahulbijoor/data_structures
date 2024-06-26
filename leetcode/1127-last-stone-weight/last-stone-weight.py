class Solution:
    #Understand
    #Time/Space
    #What if the list is empty?
    #What if the list is length 1?
    #Duplicates?

    #Match
    #Two pointers
    #Heap
    #Plan
    # Max heap
    # Take the two maximum values and compare it if equal just move on
    # Else add larger - smaller to the heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y=heapq.heappop(stones)
            x=heapq.heappop(stones)
            
            if x == y:
                continue
            
            if x!=y:
                heapq.heappush(stones,y-x)
        if len(stones)==1:
            return stones[0]*-1
        return 0

