# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # find middle
        middle = self.getMidNode(head)
        second_head = middle.next
        middle.next = None

        # reverse second list
        second_head = self.reverseLinkedList(second_head)

        # 1 -> 2 -> 3
        # 5 -> 4

        # 1 -> 2
        # 4 -> 3
        next_head_forwards = head.next
        next_head_reverse = second_head
        while next_head_forwards or next_head_reverse:
            head.next = next_head_reverse
            head = head.next
            next_head_reverse = next_head_reverse.next

            head.next = next_head_forwards
            head = head.next
            if next_head_forwards:
                next_head_forwards = next_head_forwards.next

            
    def getMidNode(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLinkedList(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
        