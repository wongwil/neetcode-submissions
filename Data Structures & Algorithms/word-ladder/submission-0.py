class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)

        wordSet = set(wordList)
        wordSet.add(beginWord)

        for word in wordSet:
            for child in wordSet:
                if word == child:
                    continue
                
                diff = 0
                for i in range(len(word)):
                    if word[i] != child[i]:
                        diff += 1

                if diff == 1:
                    graph[word].add(child)

        # now bfs
        res = 1
        q = deque()

        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return res

                for child in graph[node]:
                    if child not in visited:
                        q.append(child)
                        visited.add(child)

            res += 1

        return 0





        