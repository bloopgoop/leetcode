class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(i - k, i + k + 1):
                    if (0 <= j <= len(nums) - 1) and (len(res) == 0):
                        res.append(j)
                    if (0 <= j <= len(nums) - 1) and (j > res[-1]):
                        res.append(j)

        return res
                
                
        