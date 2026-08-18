class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mymap = Counter(tasks)

        vals = [-x for x in mymap.values()]

        heapq.heapify(vals)

        time = 0
        q = deque()
        while vals or q:
            if not vals:
                time = q[0][1] + n + 1

            if q and time - q[0][1] > n:
                nxt = q.popleft()
                heapq.heappush(vals, nxt[0])

            top = heapq.heappop(vals)
            top += 1

            if top < 0:
                q.append([top, time])

            time += 1

        return time