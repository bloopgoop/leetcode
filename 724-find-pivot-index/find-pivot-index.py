class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        if left_sum == right_sum:
            return 0

        for pivot_index in range(1, len(nums)):
            left_sum += nums[pivot_index - 1]
            right_sum -= nums[pivot_index]
            if left_sum == right_sum:
                return pivot_index
                
        return -1