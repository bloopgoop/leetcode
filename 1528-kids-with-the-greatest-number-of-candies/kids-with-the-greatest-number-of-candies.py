class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        most_candies = max(candies)
        
        for i in candies:
            result.append(i + extraCandies >= most_candies)

        return result