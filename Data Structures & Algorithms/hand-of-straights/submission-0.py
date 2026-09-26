class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        count = Counter(hand)

        for i in range(len(hand)):
            if count[hand[i]]:
                count[hand[i]] -= 1

                for j in range(hand[i]+1, hand[i]+groupSize):
                    if j not in count or not count[j]:
                        return False
                    count[j] -= 1

        return True