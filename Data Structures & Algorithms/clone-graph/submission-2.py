"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adict = {}

        def dfs(node):
            if node is None:
                return None
            if node in adict:
                return adict[node]

            adict[node] = Node(node.val, [])

            for neighbor in node.neighbors:
                adict[node].neighbors.append(dfs(neighbor))
            
            return adict[node]
        
        return dfs(node)
        