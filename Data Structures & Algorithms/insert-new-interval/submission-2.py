class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        if len(intervals) == 0:
            return [newInterval]

        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]: 
                # current interval belongs right to newInterval without overlapping
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            elif interval[1] < newInterval[0]:
                 # current interval belongs left without overlapping
                res.append(interval)
            else: 
                # current interval overlaps with new interval
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            if i == len(intervals) - 1:
                res.append(newInterval)

        return res

