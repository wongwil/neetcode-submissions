class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(','}' : '{',']' : '[' }
        stack = []
        for c in s:
            if c in pairs:
                # it's a closing parentheses
                if len(stack) == 0:
                    return False
                
                opening = stack.pop()
                if pairs[c] != opening:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0