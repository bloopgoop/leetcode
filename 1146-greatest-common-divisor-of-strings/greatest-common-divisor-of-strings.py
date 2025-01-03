class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        common_divisors = self.get_common_divisors(len(str1), len(str2))
        common_divisors.sort(reverse=True)

        for common_divisor in common_divisors:
            divisor = str1[0: common_divisor]
            if self.is_divisor(divisor, str1) and self.is_divisor(divisor, str2):
                return divisor

        return ""


    def get_common_divisors(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: list
        """
        common_divisors = []
        for i in range(1, min(n,m) + 1):
            if n % i == 0 and m % i == 0:
                common_divisors.append(i)

        return common_divisors

    def is_divisor(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 * (len(str2)/len(str1)) == str2:
            return True
        return False

        