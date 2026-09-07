class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("Inf")] * n
        dist[src] = 0

        for i in range(k+1):
            tmpDist = dist.copy()

            for u, v, w in flights:
                if tmpDist[v] > dist[u] + w:
                    tmpDist[v] = dist[u] + w

            dist = tmpDist

        if dist[dst] == float("Inf"):
            return -1

        return dist[dst]
