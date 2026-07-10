class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                smaller_temp, smaller_i = stack.pop() 

                res[smaller_i] = i - smaller_i
            
            stack.append([temp, i])
        return res