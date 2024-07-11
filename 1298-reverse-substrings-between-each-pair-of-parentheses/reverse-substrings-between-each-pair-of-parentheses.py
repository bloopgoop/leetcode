class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for index in range(len(s)):
            if s[index] == "(":
                stack.append(index)

            if s[index] == ")":
                start = stack.pop()
                s = s[:start + 1] + s[start + 1:index][::-1] + s[index:]
        
        
        s = s.replace("(", "")
        s = s.replace(")", "")

        return s