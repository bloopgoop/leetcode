class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_s = ""
        for char in s:
            if char.isalnum():
                sanitized_s += char.lower()
        
        if len(sanitized_s) == 0:
            return True
        
        l = 0
        r = len(sanitized_s) - 1

        while l < r:
            if sanitized_s[l] != sanitized_s[r]:
                return False
            l += 1
            r -= 1

        return True