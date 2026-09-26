class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0

        jumps = 0
        while r < len(nums) - 1:
            extended = r

            for i in range(l, r+1):
                extended = max(extended, i + nums[i])

            l = r+1
            r = extended
            jumps += 1

        return jumps