# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # slow is at the middle
        # reverse the last half
        prev = None
        cur = slow.next

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # find max twin
        res = 0
        while head.next:
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next

        return res
