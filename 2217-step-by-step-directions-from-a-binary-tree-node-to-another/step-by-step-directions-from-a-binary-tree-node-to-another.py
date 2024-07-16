# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        val_to_path = {}
        path = []
        
        # use list and pop when backtracking to save memory
        def dfs(root):
            if not root:
                return False

            if root.val == startValue:
                val_to_path[startValue] = path[:]
            if root.val == destValue:
                val_to_path[destValue] = path[:]

            # end early if found both start and dest
            if len(val_to_path) == 2:
                return True

            # append current direction to path, to be changed later
            path.append("")
            
            path[-1] = "L"
            dfs(root.left)

            path[-1] = "R"
            dfs(root.right)

            path.pop()

            return False

        dfs(root)

        s_path = "".join(val_to_path[startValue])
        d_path = "".join(val_to_path[destValue])

        if s_path == d_path:
            return ""

        i = 0
        while s_path[i:] and d_path[i:] and s_path[i] == d_path[i]:
            i += 1

        if not s_path[i:]:
            return d_path[i:]

        if not d_path[i:]:
            return "U" * len(s_path[i:])

        return len(s_path[i:]) * "U" + d_path[i:]