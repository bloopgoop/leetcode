class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return True
            else:
                if nums[i] == 0:
                    return False

                furthest_index = i + nums[i]
                for j in range(i + 1, furthest_index + 1):
                    if j + nums[j] >= furthest_index:
                        furthest_index = j + nums[j] 
                        i = j
