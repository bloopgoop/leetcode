# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf = []
        root2_leaf = []

        def dfs(root, leaf: int):
            if not root.left and not root.right:
                if leaf == 1:
                    root1_leaf.append(root.val)
                else:
                    root2_leaf.append(root.val)

            if root.left:
                dfs(root.left, leaf)
            if root.right:
                dfs(root.right, leaf)

        dfs(root1, 1)
        dfs(root2, 2)

        return root1_leaf == root2_leaf