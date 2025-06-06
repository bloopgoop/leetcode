class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy and sell immediately if nums[i] > nums[i - 1]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        
        return res