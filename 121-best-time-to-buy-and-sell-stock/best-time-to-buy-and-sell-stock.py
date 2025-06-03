class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l_min = prices[0]
        l_max = prices[0]

        for price in prices:
            if price < l_min:
                l_min = price
                l_max = price
            
            if price > l_max:
                l_max = price
                res = max(res, l_max - l_min)

        return res