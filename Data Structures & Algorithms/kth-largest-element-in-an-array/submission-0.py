class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-x for x in nums]
        heapq.heapify(maxheap)

        while k > 1:
            heapq.heappop(maxheap)
            k -= 1

        return -maxheap[0]
