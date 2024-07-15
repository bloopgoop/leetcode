# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class CustomTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None, parent=None):
        super(CustomTreeNode, self).__init__(val, left, right)
        self.parent = parent

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        val_to_node = {}
        root = None

        for description in descriptions:
            if description[0] not in val_to_node:
                parent = CustomTreeNode(description[0])
                if description[1] in val_to_node: # if child in hash alrdy
                    child = val_to_node[description[1]]
                else:
                    child = CustomTreeNode(description[1])

                if description[2] == 1:
                    parent.left = child
                else:
                    parent.right = child

                val_to_node[description[0]] = parent
                val_to_node[description[1]] = child
                child.parent = parent
                root = parent

            else:
                if description[1] in val_to_node: # if child in hash alrdy
                    child = val_to_node[description[1]]
                else:
                    child = CustomTreeNode(description[1])

                if description[2] == 1:
                    val_to_node[description[0]].left = child
                else:
                    val_to_node[description[0]].right = child

                val_to_node[description[1]] = child
                child.parent = val_to_node[description[0]]

        while root.parent:
            root = root.parent

        return root