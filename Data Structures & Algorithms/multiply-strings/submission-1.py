class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # e.g. 23 * 34
        # res = [0 0 0 0]

        # reverse them to go from right to left
        # 32, 43-> 3*4 = 12 (2 and 1 carry)
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = len(num1)
        m = len(num2)
        res = [0 for _ in range(n+m)]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1 + i2] += int(num1[i1]) * int(num2[i2])
                res[i1+i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] %= 10

        res = res[::-1]
        
        l = 0
        while l < n and res[l] == 0:
            l += 1

        res = res[l:]

        mystr = ""
        for num in res:
            mystr += str(num)

        return mystr

