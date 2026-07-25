class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = -1
        r = len(A) - 1

        while l <= r:
            i = (r-l) // 2 + l
            j = half - 1 - (i+1)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i < len(A) - 1 else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j < len(B) - 1 else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
                else:
                    return min(Bright, Aright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1