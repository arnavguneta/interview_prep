import math
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = 0
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                elif token == '/':
                    res = operand1 / operand2
                    if res < 0:
                        res = math.ceil(res)
                    res = math.floor(res)
                stack.append(res)
        return stack.pop()
                
s = Solution()
assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22