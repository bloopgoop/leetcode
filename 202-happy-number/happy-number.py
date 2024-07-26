class Solution:
    def isHappy(self, n: int) -> bool:
        # 1 and 7 is happy number
        if n == 1 or n == 7: return True

        while n > 9:
            sum_of_squares = 0
            while n != 0:
                sum_of_squares += (n % 10) ** 2
                n = n // 10
            n = sum_of_squares

        if n == 1 or n == 7:
            return True
        return False