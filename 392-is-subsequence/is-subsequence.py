class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        slow = 0
        for fast in range(len(t)):
            if t[fast] == s[slow]:
                slow += 1
        
            if slow == len(s):
                return True

        return False
