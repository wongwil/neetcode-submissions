class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            res = 0
            while n:
                digit = n % 10

                res += digit ** 2

                n = n // 10
            return res

        fast = n
        slow = n
        while True:
            fast = getSum(getSum(fast))
            slow = getSum(slow)

            if fast == 1:
                return True
                
            if fast == slow:
                return False

   