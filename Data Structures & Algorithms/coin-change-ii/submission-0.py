class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]

            if remain == 0:
                return 1

            if i == len(coins):
                return 0

            # skip
            res = dfs(i+1, remain)

            # take and continue
            coin = coins[i]

            if remain >= coin: 
                res += dfs(i, remain - coin)

            dp[(i, remain)] = res

            return dp[(i, remain)]

        return dfs(0, amount)



            