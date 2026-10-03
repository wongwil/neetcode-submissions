class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        carry = 1
        for i in range(len(digits)):
            digits[i] = digits[i] + carry 
            carry = digits[i] // 10

            digits[i] %= 10

        if carry:
            digits.append(carry)


        digits.reverse()

        return digits