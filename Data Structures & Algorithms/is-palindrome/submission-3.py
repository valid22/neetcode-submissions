class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_alpanum = lambda i: (ord('a') <= ord(i) <= ord('z')) or (ord('0') <= ord(i) <= ord('9'))

        i, j, N = 0, len(s) - 1, len(s)
        while i < j:
            a = s[i].lower()
            if not is_alpanum(a):
                i += 1
                continue

            b = s[j].lower()
            if not is_alpanum(b):
                j -= 1
                continue

            if a != b:
                return False

            i += 1
            j -= 1

        return True  