class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        l = 0
        r = 0
        n = len(gas)
        tank = 0
        while r < n - 1:
            tank += gas[r] - cost[r] 
            if tank < 0:
                l = r + 1
                r = l
                tank = 0
            else:
                r += 1

        return l