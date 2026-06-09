class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, 0
        s = re.sub('[^a-zA-Z0-9]', '', s)
        n = len(s)

        j = int(n / 2)
        if n % 2 == 0:
            i = j - 1
        else:
            i = int(n / 2)

        while j < n:
            if s[i].lower() != s[j].lower():
                return False
            j += 1
            i -= 1

        return True