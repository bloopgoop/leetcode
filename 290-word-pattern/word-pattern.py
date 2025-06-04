class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}

        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = words[i]
            elif pattern_to_word[pattern[i]] != words[i]:
                return False

            if words[i] not in word_to_pattern:
                word_to_pattern[words[i]] = pattern[i]
            elif word_to_pattern[words[i]] != pattern[i]:
                return False

        return True