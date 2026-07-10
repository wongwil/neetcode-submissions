class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {'}' : '{', ')' : '(', ']' : '['}
        stack = []
        for c in s:
            if c in mymap:
                # closing
                if len(stack) == 0: 
                    return False

                r = stack.pop()
                if r != mymap[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0