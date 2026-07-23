class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r - l) //  2 + l

            if nums[m] < target:
                l = m + 1
            else: # nums[m] >= target
                r = m

        if l < len(nums) and nums[l] == target:
            return l
        else:
            return -1