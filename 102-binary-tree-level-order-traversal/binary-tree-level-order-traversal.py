# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = self.level(root)
        queue = [root]
        res = []
        
        for i in range(levels):
            ints = []
            for node in queue:
                ints.append(node.val)
            res.append(ints)


            for node in queue[:]: # copy
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue.pop(0)

        return res


    def level(self, root):
        if not root:
            return 0
        
        return 1 + max(self.level(root.left), self.level(root.right))

            

            