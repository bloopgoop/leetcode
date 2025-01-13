class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_counter = 0
        while i < len(nums) - zero_counter:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zero_counter += 1
            else:
                i += 1
        