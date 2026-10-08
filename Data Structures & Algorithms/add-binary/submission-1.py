class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                b = "0" + b
        else:
            for i in range(len(b) - len(a)):
                a = "0" + a

        res = ""
        carry = [0] * (len(a) + 1)
        for i in range(len(a)-1, -1, -1):
            num = int(a[i]) + int(b[i]) + carry[i+1] 
            carry[i] = 1 if num >= 2 else 0
            res = res + str(num % 2) 

        if carry[0] > 0:
            res = res + "1"

        return res[::-1]
            


