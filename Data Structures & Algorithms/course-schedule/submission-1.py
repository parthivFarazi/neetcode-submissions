class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        

        path = set()
        visited = set()


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
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True