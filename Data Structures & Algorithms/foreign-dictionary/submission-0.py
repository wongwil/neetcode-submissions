class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for word in words for c in word}

        indegree = {c : 0 for c in graph}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minlength = min(len(w1), len(w2))
            # prefix check and length
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return "" # same prefix but w1 longer is not allowed


            for j in range(minlength):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break


        
        res = []
        q = deque()

        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        
        while q:
            c = q.popleft()
            res.append(c)

            for neigh in graph[c]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)


        for c in indegree:
            if indegree[c] != 0:
                return ""

        return "".join(res)

