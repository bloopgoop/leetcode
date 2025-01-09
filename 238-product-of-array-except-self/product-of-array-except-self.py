class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # go through array forwards and backwards
        # store all computed multiplications in a hash

        # input:
        # [1, 2, 3, 4]

        # forwards:
        # (0, 0): 1
        # (0, 1): 1
        # (0, 2): 2
        # (0, 3): 6

        # backwards:
        # (4, 4): 1
        # (3, 4): 4
        # (2, 4): 12
        # (1, 4): 24

        # answer[i] = forwards[(0, i)] * backwards[(i + 1, len(nums))]

        # store computed in a hash
        products = {}

        # forwards
        products[(0, 0)] = 1
        for i in range(1, len(nums)):
            products[(0, i)] = products[(0, i - 1)] * nums[i - 1]

        # backwards
        products[(len(nums), len(nums))] = 1
        for i in range(len(nums) - 1, 0, -1):
            products[(i, len(nums))] = products[(i + 1, len(nums))] * nums[i]

        answer = []
        for i in range(len(nums)):
            answer.append(products[(0, i)] * products[(i + 1, len(nums))])

        return answer

