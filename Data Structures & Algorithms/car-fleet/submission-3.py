class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse = True, key = lambda x : x[0])

        stack = []
        for (p, s) in pairs:
            t = (target - p) / s

            stack.append(t)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)