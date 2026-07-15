# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        if root is None:
            return []
        
        q = deque()
        q.append(root)

        answer = []
        while q:
            level_length = len(q)
            level = []

            for i in range(level_length):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            answer.append(level[-1])
            level = []
        return answer


        