class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            x, y = s[i], t[i]
            count_s[x] = count_s.get(x, 0) + 1
            count_t[y] = count_t.get(y, 0) + 1
        
        return count_s == count_t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            g = tuple(sorted(s))
            if g not in groups:
                groups[g] = [s]
            else:
                if self.isAnagram(s, groups[g][-1]):
                    groups[g].append(s)
        
        return list(groups.values())