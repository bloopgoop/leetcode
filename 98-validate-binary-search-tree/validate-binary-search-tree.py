# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True

            if not (node.val > minimum and node.val < maximum):
                return False

            # when we go left, the minimum does not change; when we go right, the maximum does not change
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

        return valid(root, float('-inf'), float('inf'))