class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        parent = [i for i in range(n + 1)] # need +1 because the indeces start at 1...

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


            # here you could do some balancing with ranks but skipped for simplicity
            # e.g. that the one group with more items stays the root
            parent[rootV] = rootU
            return True

    
        for u,v in edges:
            if not union(u,v):
                return [u, v]
