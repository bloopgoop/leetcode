# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even_head, recent_even = head, head
        odd_head, recent_odd = head.next, head.next

        i = 1
        cur = head.next

        while cur.next:
            i += 1
            cur = cur.next

            if i % 2 == 0:
                recent_even.next = cur
                recent_even = recent_even.next 
            else:
                recent_odd.next = cur
                recent_odd = recent_odd.next

        recent_even.next = odd_head
        recent_odd.next = None
        return even_head