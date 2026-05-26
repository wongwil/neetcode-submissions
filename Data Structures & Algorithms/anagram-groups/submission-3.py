class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            cnts = [0] * 26

            for c in s:
                cnts[ord(c) - ord('a')] += 1
            
            seen[tuple(cnts)].append(s)

        return list(seen.values())

        
