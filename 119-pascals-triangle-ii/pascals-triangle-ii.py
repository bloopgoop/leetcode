class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def fact(n):
            if n == 0:
                return 1
            for i in range(1, n):
                n = n * i
            return n

        def choose(n, k):
            return fact(n) / (fact(n - k) * fact(k))
        
        res = []
        for k in range(rowIndex):
            res.append(choose(rowIndex, k))
        res.append(1)
        return res