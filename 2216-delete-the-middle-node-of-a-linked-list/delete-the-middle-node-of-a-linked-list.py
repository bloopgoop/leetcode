# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # case where there is only 1 Node
        if slow.next == None:
            return None

        # slow is now at the Node before the one to delete
        slow.next = slow.next.next
        
        return head
