# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        fast, slow = head, head
        total = 0
        fast = fast.next
        while fast:

            while fast.val != 0:
                total += fast.val
                fast = fast.next

            slow.val = total
            total = 0
            slow.next = fast
            fast = fast.next
            if not fast:
                slow.next = None
            slow = slow.next

        return head


        