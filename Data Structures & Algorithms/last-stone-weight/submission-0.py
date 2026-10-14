from bisect import insort

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = deque(sorted(stones))

        while len(s) > 1:
            a, b = s.pop(), s.pop()
            if a > b:
                insort(s, (a-b))
        
        return s[0] if s else 0

