class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l_min = prices[0]
        l_max = prices[0]

        # first pass, find local min and maxes
        for price in prices:
            if price < l_max:
                # l_max was the local max, sell the stock
                res += l_max - l_min
                l_max = price
                l_min = price
            else:
                l_max = price
            
            if price > l_min:
                # l_min was the local min
                pass
            else:
                l_min = price

        if l_max > l_min:
            res += l_max - l_min

        return res