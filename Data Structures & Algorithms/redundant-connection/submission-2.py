class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            root = parent[x]

            while root != parent[root]:
                root = parent[root]

            return root


        def union(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return False


            parent[rootV] = rootU

            return True


        for u,v  in edges:
            if not union(u,v):
                return [u, v]

        