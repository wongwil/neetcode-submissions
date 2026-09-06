class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for word in words for c in word}
        indegree = {c : 0 for c in graph}
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break


        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)

            for n in graph[c]:
                indegree[n] -= 1

                if indegree[n] == 0:
                    q.append(n)

        if len(res) < len(indegree):
            return ""

        return "".join(res)
