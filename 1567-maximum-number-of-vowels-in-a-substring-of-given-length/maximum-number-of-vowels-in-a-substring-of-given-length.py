class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        l = 0
        r = k - 1
        vowel_count = 0
        for i in range(r + 1):
            if s[i] in vowels:
                vowel_count += 1
        res = vowel_count
        l += 1
        r += 1
        if res == k:
            return res

        while r < len(s):
            if s[r] in vowels:
                vowel_count += 1
            if s[l - 1] in vowels and l != r:
                vowel_count -= 1
            res = max(res, vowel_count)
            if res == k:
                return res
            l += 1
            r += 1

        return res