class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjm = [[] for _ in range(n)]

        for u,v in edges:
            adjm[u].append(v)
            adjm[v].append(u)

        visiting = set()
        def dfs(i, parent):
            if i in visiting:
                return False

            visiting.add(i)
            for child in adjm[i]:
                if child == parent:
                    continue

                if not dfs(child, i):
                    return False

            
            return True



        if not dfs(0, None):
            return False

        return len(visiting) == n
