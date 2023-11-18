class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        match = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i, c in enumerate(s):
            if c == '(' or c == '[' or c == '{':
                open_stack.append(c)
            else:
                if len(open_stack) == 0 or c != match[open_stack.pop()]: return False

        return len(open_stack) == 0
        
