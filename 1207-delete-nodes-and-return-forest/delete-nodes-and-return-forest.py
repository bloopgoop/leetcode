# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        roots = []

        if root.val not in to_delete:
            roots.append(root)

        def dfs(root):
            if not root:
                return

            left = root.left
            if left and left.val in to_delete:
                root.left = None
            dfs(left)

            right = root.right
            if right and right.val in to_delete:
                root.right = None
            dfs(right)


            if root.val in to_delete:
                if root.left:
                    roots.append(root.left)
                if root.right:
                    roots.append(root.right)

        dfs(root)
        return roots
