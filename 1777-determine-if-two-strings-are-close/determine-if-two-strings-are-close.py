class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # dict of char to occurence of word1
        count1 = {}
        for char in word1:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1

        # dict of char to occurence of word2
        count2 = {}
        for char in word2:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        # if keys arent the same, it's not close
        if set(count1.keys()) != set(count2.keys()):
            return False

        
        # if the occurences aren't the same, it's not close
        if sorted(list(count1.values())) != sorted(list(count2.values())):
            return False

        return True