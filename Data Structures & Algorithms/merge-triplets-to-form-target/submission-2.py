class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstFound = False
        secondFound = False
        thirdFound = False

        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                firstFound = True
            
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                secondFound = True

            if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                thirdFound = True


        return firstFound and secondFound and thirdFound