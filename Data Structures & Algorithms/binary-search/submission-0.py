class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            c = int((r - l) / 2) + l

            if target == nums[c]:
                return c
            elif nums[c] < target:
                l = c + 1
            else:
                r = c - 1
        
        return -1
    
        