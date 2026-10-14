import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = []

        for i in points:
            x, y = i
            heapq.heappush(p, ( x ** 2 + y ** 2, i ))
        

        return [heapq.heappop(p)[1] for i in range(k)]