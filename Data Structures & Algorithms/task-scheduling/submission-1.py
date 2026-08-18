class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mymap = Counter(tasks)

        vals = [-x for x in mymap.values()]

        heapq.heapify(vals)

        time = 0
        q = deque() # pairs of [-cnt, timestamp]
        while vals or q:
            if not vals: # skip time
                time = q[0][1] + n + 1

            if q and time - q[0][1] > n: # next process is available from queue
                nxt = q.popleft()
                heapq.heappush(vals, nxt[0])

            # greedy
            top = heapq.heappop(vals)
            top += 1 # process

            if top < 0: # if not fully processed, go to queue
                q.append([top, time])

            # next time
            time += 1

        return time