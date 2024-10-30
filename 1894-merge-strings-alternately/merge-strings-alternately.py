class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        res = ""
        done1, done2 = False, False
        while True:
            try:
                res += word1[i]
            except IndexError:
                done1 = True

            try:
                res += word2[i]
            except IndexError:
                done2 = True

            i += 1

            if done1 and done2:
                return res
        