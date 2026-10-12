class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        close_stack = []
        
        for p, i in enumerate(s):
            if i == "(":
                stack.append(p)
            elif i == ")":
                if not stack:
                    close_stack.append(p)
                else:
                    stack.pop(-1)
        
        stack = set(stack)
        close_stack = set(close_stack)
        a =  "".join(s[i] for i in range(len(s)) if i not in stack and i not in close_stack)
        return a