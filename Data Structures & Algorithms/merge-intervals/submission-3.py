class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda k: k[0])
        currentInterval = intervals[0]

        res = []
        for interval in intervals:
            if currentInterval[1] >= interval[0]:
                # currentinterval is overlapping
                currentInterval[1] = max(interval[1], currentInterval[1])
            else:
                # currentinterval is left
                res.append(currentInterval)
                currentInterval = interval

                # right side can never happen since we sorted it

        res.append(currentInterval)
        return res