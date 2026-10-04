class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        res = [0] * (n+m)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i1 in range(n):
            for i2 in range(m):
                res[i1 + i2] += int(num1[i1]) * int(num2[i2])
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] %= 10

        res = res[::-1]
        l = 0
        while l < n and res[l] == 0:
            l += 1

        res = res[l:]

        return "".join([str(i) for i in res])