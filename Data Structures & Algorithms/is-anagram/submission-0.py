class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = (s, t) if len(s) < len(t) else (t, s)
        count = {}

        n1, n2 = len(s), len(t) - len(s)
        for i in range(n1):
            x, y = s[i], t[i]
            count[x] = count.get(x, 0) + 1
            count[y] = count.get(y, 0) - 1
        
        for i in range(n2):
            x, y = s[i], t[i]
            count[x] = count.get(x, 0) + 1
            count[y] = count.get(y, 0) - 1
        
        for i in count.values():
            if i:
                return False

        return True

