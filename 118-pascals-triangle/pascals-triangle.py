class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # each cell in pascals triangle equates to nCk or n choose k, 
        # where n is the nth row and k is how many to choose from
        def fact(n):
            if n == 0:
                return 1
            for i in range(1, n):
                n = n * i
            return n

        def choose(n, k):
            return fact(n) / (fact(n-k) * fact(k))

        res = []
        for n in range(0, numRows):
            row = []
            for k in range(n + 1):
                row.append(choose(n, k))
            res.append(row)
        return res
