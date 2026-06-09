class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

         
        res = []
        for i, z in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]

                if curr < -z:
                    l += 1
                elif curr > -z:
                    r -= 1
                else:
                    res.append([z, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        ## move until we find a new number to prevent
                        ## duplicates
                        l += 1

        return res