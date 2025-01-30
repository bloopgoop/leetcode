class Solution:
    def decodeString(self, s: str) -> str:

        # if all the characters in s is alphabetical:
        #   return s

        # open the first bracket with x times
        #   return x * self.decodeString(stringInsideBracket)

        # find the first instance of numeric character, get the last instance before bracket
        
        res = ""
        substring = ""
        multiple = ""
        stack = []
        for char in s:
            if stack:
                if char == "]":
                    stack.pop(-1)
                    if not stack:
                        res += int(multiple) * self.decodeString(substring)
                        substring = ""
                        multiple = ""
                    else:
                        substring += char

                else:
                    if char == "[":
                        stack.append("[")
                    substring += char

            else:
                if char.isnumeric():
                    multiple += char
                elif char == "[":
                    stack.append("[")
                else:
                    res += char

        return res
