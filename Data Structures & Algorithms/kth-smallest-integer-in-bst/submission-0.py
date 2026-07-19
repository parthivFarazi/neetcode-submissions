# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.answer = None
        self.count = 0

        def inOrderTrav(node):
            if node is None or self.answer is not None:
                return
            inOrderTrav(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return 
            inOrderTrav(node.right)
            return node
        
        inOrderTrav(root)
        return self.answer

        