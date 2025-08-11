# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    root = None
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #print("preorder",preorder)
        #print("inorder", inorder)
        if not preorder or not inorder:
            return None

        if preorder[0] == inorder[0] and len(inorder) == 1:
            return TreeNode(val = preorder[0], left = None, right = None)
        root = TreeNode(val = preorder[0], left = None, right = None)

        root_index_inorder = inorder.index(preorder[0])
        #print(root_index_inorder)
        root.left = self.buildTree(preorder[1:], inorder[:root_index_inorder])
        
        if root_index_inorder >= len(preorder) or root_index_inorder >=len(inorder):
            return None
        root.right = self.buildTree(preorder[root_index_inorder + 1:], inorder[root_index_inorder + 1:])

        return root