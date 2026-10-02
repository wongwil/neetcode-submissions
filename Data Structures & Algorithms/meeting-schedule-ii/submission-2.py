"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1)) # new room
            events.append((interval.end, -1)) # close room

        events.sort()
        sametime = 0
        res = 0
        for event in events:
            sametime += event[1]
            res = max(res, sametime)

        return res