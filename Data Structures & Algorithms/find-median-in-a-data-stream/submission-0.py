class MedianFinder:

    def __init__(self):
        # given sorted numbers [x ... y] we partition such that [x .. ] [... y]
        self.maxheap = [] # keep track of the largest k elements of the left numbers
        self.minheap = [] # keep track of the smallest m elements of the right numbers

    def addNum(self, num: int) -> None:
        # always move the largest number in left half to the right half
        heapq.heappush(self.maxheap, -num)

        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        # always keep left heap 1 larger of same size
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]
        