class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return jumps
            elif i + nums[i] >= len(nums) - 1:
                return jumps + 1
            else:
                furthest_index = i + nums[i]
                for j in range(i + 1, furthest_index + 1):
                    if j + nums[j] >= furthest_index:
                        furthest_index = j + nums[j] 
                        i = j
                jumps += 1