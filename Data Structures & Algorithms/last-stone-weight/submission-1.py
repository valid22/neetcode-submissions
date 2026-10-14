import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for i in stones:
            heapq.heappush(s, -i)
        

        while len(s) > 1:
            a, b = -heapq.heappop(s), -heapq.heappop(s)
            if a > b:
                heapq.heappush(s, -(a - b))
        
        return -heapq.heappop(s) if s else 0

