class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]

        if len(word1) > len(word2):
            res += word1[len(word2):]
        else:
            res += word2[len(word1):]

        return res