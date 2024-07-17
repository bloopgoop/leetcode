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
        to_delete = set(to_delete) # O(1) lookups
        forest = []

        root = self._process_node(root, to_delete, forest)

        if root:
            forest.append(root)
        
        return forest

    def _process_node(self, node, to_delete, forest):
        if not node:
            return None

        node.left = self._process_node(node.left, to_delete, forest)
        node.right = self._process_node(node.right, to_delete, forest)

        # Node evaluation: Check if the current node needs to be deleted
        if node.val in to_delete:
            # If the node has left or right children, add them to the forest
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            # Delete the current node by returning None to its parent
            return None

        return node