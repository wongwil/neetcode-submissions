class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for i in nums:
            cnts[i] += 1

        groups = [[] for _ in range(len(nums) + 1)]

        for key, cnt in cnts.items():
            groups[cnt].append(key)

        res = []
        for group in groups[::-1]:
            for key in group:
                res.append(key)

                if len(res) == k:
                    return res
