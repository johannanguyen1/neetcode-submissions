# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # count_nodes = root.length()
        # count_layers = math.log(count_nodes, 2)

        if not root:
            return None

        if root: 
            temp = root.left
            root.left = root.right
            root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root


        