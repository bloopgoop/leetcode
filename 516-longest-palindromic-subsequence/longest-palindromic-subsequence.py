class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp approach for SUBSEQUENCE
        # 2d array lookup

        n = len(s)
        dp = [[0]*n for _ in range(n)]

        # diagonals are 1 because any s[i:i] longestPalindroimeSubseq is 1
        for i in range(n-1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]