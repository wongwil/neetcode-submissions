class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        
        # course -> preq (children)

        # we want reversed topological order (preq first to finish all courses)

        visiting = set()
        visited = set() # all already processed
        res = []
        def dfs(i):
            if i in visiting: # visiting is for cycle detection
                return False

            if i in visited:
                return True

            visiting.add(i)
            for preq in graph[i]:
                if not dfs(preq):
                    return False
            visiting.remove(i)
            
            # every preq can be done -> this course is fine
            visited.add(i)
            res.append(i)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
        