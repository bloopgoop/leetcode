class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = set()

        # find all keys
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(i - k, i + k + 1):
                    if 0 <= j <= len(nums) - 1:
                        res.add(j)
        return sorted(res)
                