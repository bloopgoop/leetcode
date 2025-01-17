class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        total = sum(nums[l : k])
        res = total / k
        while r < len(nums):
             total += (nums[r] - nums[l])
             res = max(res, total / k)
             l += 1
             r += 1
        return res


             
        