class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mod 2
        res = 0
        while n > 0:
            if n % 2 == 1:
                res += 1
            n = n // 2
        return res