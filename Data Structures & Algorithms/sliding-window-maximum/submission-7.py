class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myheap = [] # (-val, position i)

        res = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(myheap, (-nums[r], r))

            if r < k - 1:
                continue


            while myheap[0][1] <= r - k:
                heapq.heappop(myheap)

            res.append(-myheap[0][0])
        return res