class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        pivot = 0
        while l < r:
            m = (r - l) // 2 + l

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        if nums[pivot] <= target and target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1

        while l < r:
            m = (r - l) // 2 + l

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if target == nums[l]:
           return l
        
        return -1