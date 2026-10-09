class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_l = 0
        sc = set()
        si = 0

        for i in range(len(s)):
            while s[i] in sc:
                sc.discard(s[si])
                si += 1
            else:
                sc.add(s[i])
                max_l = max(max_l, (i - si) + 1)
        
        return max_l