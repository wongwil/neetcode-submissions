class Solution:
    def canJump(self, nums: List[int]) -> bool:
        star = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= star:
                star = i

        return star == 0
