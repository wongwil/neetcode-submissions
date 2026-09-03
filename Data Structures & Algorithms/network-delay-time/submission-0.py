class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k = k-1 # 0 index

        for i in range(len(times)):
            (u, v, t) = times[i]
            times[i] = (u-1, v-1, t) # 0 index

        graph = defaultdict(list)

        for time in times:
            (u, v, t) = time
            graph[u].append((v, t))

        dist = [float("inf")] * n
        dist[k] = 0

        heap = [(dist[k], k)]

        while heap:
            d, node = heapq.heappop(heap)

            if dist[node] < d:
                continue

            dist[node] = d

            for v, t in graph[node]:
                if dist[node] + t < dist[v]:
                    heapq.heappush(heap, (dist[node] + t, v))
                    dist[v] = dist[node] + t


        minTime = max(dist)

        if minTime == float("inf"):
            return -1

        return minTime