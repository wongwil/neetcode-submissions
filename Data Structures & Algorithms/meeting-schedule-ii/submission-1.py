"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        processedHeap = []
        res = 0

        intervals.sort(key=lambda x:(x.start, x.end))
        for interval in intervals:
            if not processedHeap:
                processedHeap.append(interval.end)
            else:
                if processedHeap[0] > interval.start:
                    # overlap
                    heapq.heappush(processedHeap, interval.end)
                else:
                    heapq.heappop(processedHeap) # room can be used
                    heapq.heappush(processedHeap, interval.end)

            res = max(res, len(processedHeap))


        return res