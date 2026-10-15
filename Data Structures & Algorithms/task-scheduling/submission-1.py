from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mf = 0
        mfc = 0
        f = {}

        for i in tasks:
            f[i] = f.get(i, 0) + 1
            if f[i] > mf:
                mf = f[i]
                mfc = 1
            elif f[i] == mf:
                mfc += 1

        return max(len(tasks), (mf - 1) * (n + 1) + mfc)
