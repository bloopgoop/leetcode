# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        res = curr = ListNode()
        while l1 and l2:
            curr.next = ListNode(val=(l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

            oldval = curr.val
            curr.val = (oldval + carry) % 10
            carry = (oldval + carry) // 10

        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

            oldval = curr.val
            curr.val = (oldval + carry) % 10
            carry = (oldval + carry) // 10

        if carry:
            curr.next = ListNode(val=carry)
        
        return res.next

