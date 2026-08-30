class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # is there a cycle in the graph

        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()
    
        def dfs(i):
            if i in visited:
                return False

            visited.add(i)
            for child in graph[i]:
                if not dfs(child):
                    return False

            visited.remove(i)

            # this course is safe, we can remove all prerequisites for optimization
            # if we land on this again, we can instantly return true
            # since we know i does not require any preqreqs 
            # could also use a visited / visiting set
            graph[i] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False


        return True