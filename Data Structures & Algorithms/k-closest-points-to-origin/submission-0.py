class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclDistanceToZero(x, y):
            return math.sqrt(x**2 + y**2)
        myheap = [(euclDistanceToZero(x,y), [x, y]) for x, y in points]

        heapq.heapify(myheap)

        res = []

        while k:
            res.append(heapq.heappop(myheap)[1])
            k -= 1

        return res