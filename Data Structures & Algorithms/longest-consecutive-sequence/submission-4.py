class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            res = max(res, count)
            for j in range(i+1, len(nums), 1):
                if nums[j] - curr == 1:
                    count += 1
                    res = max(res, count)
                    curr = nums[j]

        return res