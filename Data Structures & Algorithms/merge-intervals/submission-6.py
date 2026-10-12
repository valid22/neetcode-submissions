class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)
        merged = []
        
        i = 0
        while i < len(s):
            p, q = s[i]
            while i < len(s)-1 and s[i+1][0] <= q:
                i += 1
                q = max(q, s[i][1])

            merged.append([p, q])

            i += 1

        return merged