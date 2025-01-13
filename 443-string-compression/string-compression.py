class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        char = chars[0]
        dupes = 0

        while i < len(chars) - 1:
            # print("i: {}, char: {}, dupes: {}, chars: {}".format(i, char, dupes, chars))
            
            if chars[i] != chars[i + 1]:
                if dupes > 0:
                    # compress if dupes > 0
                    for digit in str(dupes + 1)[::-1]:
                        chars.insert(i + 1, digit)
                    i += len(str(dupes + 1)) + 1
                else:
                    i += 1
                    
                dupes = 0
                char = chars[i]

            else:
                dupes += 1
                chars.pop(i + 1)

        if dupes > 0:
            for digit in str(dupes + 1)[::-1]:
                chars.insert(i + 1, digit)

        return len(chars)