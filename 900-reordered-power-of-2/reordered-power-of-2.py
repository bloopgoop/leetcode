class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        import math
        digits = len(str(n))

        powers_of_two_with_same_digits = []
        start = int(math.log(n, 2))

        i = start
        while len(str(2**i)) == digits:
            powers_of_two_with_same_digits.append(str(2**i))
            i -= 1
        i = start + 1
        while len(str(2**i)) == digits:
            powers_of_two_with_same_digits.append(str(2**i))
            i += 1
        
        # get chars to occurence in n
        n_map = {}
        for char in str(n):
            if char not in n_map:
                n_map[char] = 1
            else:
                n_map[char] += 1

        # compare with each power of 2
        for num_str in powers_of_two_with_same_digits:
            num_to_digits = {}
            for char in str(num_str):
                if char not in num_to_digits:
                    num_to_digits[char] = 1
                else:
                    num_to_digits[char] += 1

            if n_map == num_to_digits:
                return True
        
        return False
            