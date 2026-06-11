# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        left = 0
        right = 0
        if not root: 
            print("what")

            return 0
        if root: 
            if root.left: 
                left = self.maxDepth(root.left)
            if root.right: 
                right = self.maxDepth(root.right) 
        count = 1 + max(left, right)
        return count 
        