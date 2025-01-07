class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # get the positions of the vowel
        pos_to_vowel = {}
        for pos in range(len(s)):
            if s[pos].capitalize() in ["A", "E", "I", "O", "U"]:
                pos_to_vowel[pos] = s[pos]

        # get the string as a list
        mutable_s = list(s)

        # get the vowel positions as a sorted list
        vowel_pos = sorted(pos_to_vowel.keys())

        # switch vowels using two pointer
        start = 0
        end = len(vowel_pos) - 1
        while start < end:
            mutable_s[vowel_pos[start]] = pos_to_vowel[vowel_pos[end]]
            mutable_s[vowel_pos[end]] = pos_to_vowel[vowel_pos[start]]
            start += 1
            end -= 1
        
        # return list as a string
        return "".join(mutable_s)
