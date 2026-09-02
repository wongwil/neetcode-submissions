class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append(beginWord)

        visited = set()
        visited.add(beginWord)
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return res
                
                for word in wordList:
                    if word not in visited and self.isNeigh(node, word):
                        q.append(word)
                        visited.add(word)

        return 0

    def isNeigh(self, a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1

        return diff == 1