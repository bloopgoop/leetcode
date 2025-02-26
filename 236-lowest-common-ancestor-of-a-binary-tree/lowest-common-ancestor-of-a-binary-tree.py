# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        When called on the root of a binary tree, 2 cases can happen:

            case 1: p or q is on the left of the root, and the other variable is on the right of the root

                solution: return the root


            case 2: p and q are both either in the left of the root or the right of the root

                solution: find the first occurence of either p or q and return that
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right    
        
