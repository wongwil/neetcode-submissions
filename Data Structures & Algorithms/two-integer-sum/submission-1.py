class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen.get(target-nums[i]), i]
            else:
                seen[nums[i]] = i