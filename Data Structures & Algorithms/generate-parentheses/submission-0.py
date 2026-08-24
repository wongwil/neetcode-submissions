class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opens, closed, subRes):
            if opens == closed == n:
                res.append("".join(subRes.copy()))
            if opens > n:
                return

            if closed > opens:
                return

            subRes.append("(")
            dfs(opens+1, closed, subRes)

            subRes.pop()

            
            subRes.append(")")
            dfs(opens, closed+1, subRes)
            subRes.pop()

        
        dfs(0, 0, [])

        return res


            
