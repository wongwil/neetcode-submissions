class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if target <= nums[m]:
                r = m
            else:
                l = m + 1
                

        if target == nums[l]:
            return l

        return -1