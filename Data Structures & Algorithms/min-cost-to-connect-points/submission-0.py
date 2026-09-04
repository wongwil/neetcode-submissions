class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        T = set()
        node = 0

        T.add(node)

        distance = [float("Inf")] * n

        def calcDistance(a, b):
            ax, ay = a
            bx, by = b

            return abs(ax - bx) + abs(ay - by)

        res = 0
        while len(T) < n:
            nextNode = -1

            for i in range(n):
                if i in T:
                    continue

                dist = calcDistance(points[i], points[node])
                distance[i] = min(distance[i], dist)

                if nextNode == -1 or distance[i] < distance[nextNode]:
                    nextNode = i
                    
            node = nextNode
            res += distance[node]
            T.add(nextNode)


        return res


                