# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head.next.next:
            return [-1, -1]

        slow = head
        med = head.next
        fast = head.next.next

        index = 1
        criticals = []

        while fast:
            if slow.val < med.val > fast.val or slow.val > med.val < fast.val:
                criticals.append(index)
            fast = fast.next
            med = med.next
            slow = slow.next
            index += 1

        if len(criticals) < 2:
            return [-1, -1]

        minDistance = maxDistance = criticals[-1] - criticals[0]
        for i in range(len(criticals) - 1):
            minDistance = min(minDistance, criticals[i + 1] - criticals[i])

        return [minDistance, maxDistance]
