from collections import deque

class Solution:
    def do_math(self, a, b, o):
        match o:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()

        op = {'+', '-', '*', '/'}
        for i in tokens:
            if i in op:
                b, a = s.pop(), s.pop()
                s.append(self.do_math(a, b, i))
            
            else:
                s.append(int(i))


        return s[0]
