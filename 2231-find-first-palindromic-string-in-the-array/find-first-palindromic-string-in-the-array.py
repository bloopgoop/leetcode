class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            reverse = word[::-1]
            if reverse == word:
                return word
        return ""