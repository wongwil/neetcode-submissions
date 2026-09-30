class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        lastInterval = intervals[0]

        res = 0
        for interval in intervals[1:]:
            # last interval overlaps with current one
            # e.g. [1,7] [2, 6]
            if lastInterval[1] > interval[0]:
                res += 1
                lastInterval[1] = min(lastInterval[1], interval[1])
            else:
                lastInterval = interval

        return res