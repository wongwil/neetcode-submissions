class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                # add
                x = stack.pop()
                y = stack.pop()

                stack.append(y + x)
            elif c == '-':
                # min
                x = stack.pop()
                y = stack.pop()

                stack.append(y - x)
            elif c == '/':
                # div
                x = stack.pop()
                y = stack.pop()

                stack.append(int(y / x))
            elif c == '*':
                # multiply
                x = stack.pop()
                y = stack.pop()

                stack.append(y * x)
            else:
                # number
                stack.append(int(c))

        return stack[-1]