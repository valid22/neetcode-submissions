class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        window = {}

        for c in s1:
            target[c] = target.get(c, 0) + 1

        k = len(s1)

        for i, c in enumerate(s2):
            # add current character
            window[c] = window.get(c, 0) + 1

            # remove character that is now outside the window
            if i >= k:
                left = s2[i - k]
                window[left] -= 1

                if window[left] == 0:
                    del window[left]

            # compare
            if window == target:
                return True

        return False
