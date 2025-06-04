class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right_products = [nums[0] for _ in range(len(nums))]
        right_to_left_products = [nums[-1] for _ in range(len(nums))]

        for i in range(1, len(nums)):
            left_to_right_products[i] = left_to_right_products[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            right_to_left_products[i] = right_to_left_products[i + 1] * nums[i]

        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                res[i] = right_to_left_products[i + 1]
            elif i == len(nums) - 1:
                res[i] = left_to_right_products[i - 1]
            else:
                res[i] = left_to_right_products[i - 1] * right_to_left_products[i + 1]

        return res