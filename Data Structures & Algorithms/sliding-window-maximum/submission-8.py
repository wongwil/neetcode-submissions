class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myheap = [] # (-val, position i)

        res = []

        for r in range(len(nums)):
            # push element in heap
            heapq.heappush(myheap, (-nums[r], r))

            # we haven't reached a window yet of size k
            if r < k - 1:
                continue

            # we remove the head of the heap when it's old (outside of the window)
            while myheap[0][1] <= r - k:
                heapq.heappop(myheap)

            # we add the max element to the result
            res.append(-myheap[0][0])

        return res