class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse = True, key = lambda x : x[0])

        res = 0
        lastmin = float("-Inf")
        for (p, s) in pairs:
            t = (target - p) / s

            if t > lastmin:
                res += 1
                lastmin = t

        return res