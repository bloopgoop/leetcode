class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1

            if r - l + 1 > res:
                res = r - l + 1
        
        return res
            