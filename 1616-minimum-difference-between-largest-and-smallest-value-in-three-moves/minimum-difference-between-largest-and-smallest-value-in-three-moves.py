class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0

        # sort
        nums.sort()

        # check every combination of total 3 elements removed from beginning or last
        # almost same concept as sliding window
        # 0, 3 <- 0 removed from beginning, 3 removed from end
        # 1, 2
        # 2, 1
        # 3, 0
        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4-i)] - nums[i])
        return ans


        