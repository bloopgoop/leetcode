# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        """
        level from root: 2 (root, 1 down from root, 2 down from root)

        [10] -> 0

        -3

        [7, -3] -> 0

        + 11

        [18, 8, 11] -> 1

        """
        
        res = [0]

        def dfs(root, sums: list):
            if not root:
                return

            # add current node val to every entry in list and append current node val
            for i in range(len(sums)):
                sums[i] += root.val
            sums.append(root.val)

            # check if there is a path with targetSum 
            for s in sums:
                if s == targetSum:
                    res[0] += 1

            dfs(root.left, sums)
            dfs(root.right, sums)

            # undo adding current node val before call back
            sums.pop(-1)
            for i in range(len(sums)):
                sums[i] -= root.val

        dfs(root, [])

        return res[0]