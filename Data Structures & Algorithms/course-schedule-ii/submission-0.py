
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {}


        for i in range(numCourses):
            graph[i] = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)



        path = set()
        visited = set()
        revAnswer = []

        def dfs(node):
            if node in path:
                return False

            if node in visited:
                return True

            path.add(node)

            for child in graph[node]:
                if not dfs(child):
                    return False

            path.remove(node)
            visited.add(node)
            revAnswer.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        answer = revAnswer[::-1]
        return answer

# O(V + E) time and space
# 17 mins 21 secs
        