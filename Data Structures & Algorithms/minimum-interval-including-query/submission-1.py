class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort both lists and process queries from left to right



        # use a min heap to save (size, end)
        # while interval.start < q => push to heap
        # pop if end < q
        # else take the top (shortest size)

        # keep a map to return result in original order

        intervals.sort()
        minheap = []
        res = {}
        l = 0
        for q in sorted(queries):
            while l < len(intervals) and intervals[l][0] <= q:
                heapq.heappush(minheap, (intervals[l][1] - intervals[l][0] + 1, intervals[l][1]))
                l += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            if minheap:
                res[q] = minheap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]

