class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(i):
            if visited[i]: 
                return

            visited[i] = True
            for child in adj[i]:
                dfs(child)


        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res