
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        
        for i in range(n):
            graph[i] = []

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        seen = set()
        counter = 0

        def dfs(i):
            if i in seen:
                return

            seen.add(i)

            for neighbor in graph[i]:
                dfs(neighbor)

            return

        for i in range(n):
            if i not in seen:
                dfs(i)
                counter += 1

        return counter

# O(V + E) time and space
# 31 mins 14 secs