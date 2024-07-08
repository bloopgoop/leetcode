# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_to_index = {}

        counter = 0
        while head:
            if head in node_to_index:
                return True
            else:
                node_to_index[head] = counter
            
            counter += 1
            head = head.next
        
        return False