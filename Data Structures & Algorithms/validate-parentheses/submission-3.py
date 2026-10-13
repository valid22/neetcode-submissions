from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        start = set('[({')
        end = {')': "(", "}": "{", "]": "["}
        for i in s:
            if i in start:
                stack.append(i)
            
            if i in end:
                # print(f"{i = }, {end[i] = }, {stack[-1] = }")
                if not stack or end[i] != stack[-1]:
                    return False
                
                stack.pop()
        
        return not len(stack)