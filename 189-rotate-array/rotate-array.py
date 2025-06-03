class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # handle k > n
        temp = nums.copy()

        for i in range(n - k, n):
            nums[i - (n - k)] = temp[i]

        for i in range(n - k):
            nums[i + k] = temp[i]