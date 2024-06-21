class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # hash all numbers
        appearances = {}
        for num in nums:
            if num not in appearances:
                appearances[num] = 1
            else:
                appearances[num] += 1

        for key in appearances:
            if appearances[key] == 1:
                return key