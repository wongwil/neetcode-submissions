"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x : (x.start, x.end))

        lastInterval = intervals[0]
        for interval in intervals[1:]:
            if lastInterval.end > interval.start:
                return False

            lastInterval = interval


        return True