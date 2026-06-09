class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            leftn = numbers[l]
            rightn = numbers[r]

            if leftn + rightn == target:
                return [l+1, r+1]
            elif leftn + rightn < target:
                l += 1
            else:
                r -= 1