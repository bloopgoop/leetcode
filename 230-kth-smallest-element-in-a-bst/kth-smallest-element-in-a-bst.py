# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        res = [0]

        # in order traversal
        def iot(root):
            if not root:
                return
            
            iot(root.left)
            count[0] += 1
            if count[0] == k:
                res[0] = root.val
            iot(root.right)

        iot(root)
        return res[0] 
            
