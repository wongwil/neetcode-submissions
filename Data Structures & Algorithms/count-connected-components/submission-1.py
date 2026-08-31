class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(i, parent):
            if i in visited:
                return

            visited.add(i)

            for child in adj[i]:
                if child == parent:
                    continue
                dfs(child, i)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1

        return res