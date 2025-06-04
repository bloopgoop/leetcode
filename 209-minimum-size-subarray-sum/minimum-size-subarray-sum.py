class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        res = float('inf')
        s = l = 0
        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        
        return res