"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        # map real to clone
        clone = {}

        # 1 pass to initialize mapping
        cur = head
        while cur:
            clone[cur] = Node(0)
            cur = cur.next

        # 2nd pass to build the deep copy      
        cur = head
        while cur:
            clone[cur].next = clone[cur.next] if cur.next else None
            clone[cur].random = clone[cur.random] if cur.random else None
            clone[cur].val = cur.val
            cur = cur.next
        
        return clone[head]

        