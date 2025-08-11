class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        # turn it into binary
        powers = []
        while n:
            lowBit = n & -n
            #print(lowBit)
            powers.append(lowBit)
            n ^= lowBit
            #print(n)

        #print(powers)
        size = len(powers)
        table = [[0] * size for _ in range(size)]
        for row, val in enumerate(powers):
            table[row][row] = val
            for col in range(row + 1, size):
                table[row][col] = (
                    table[row][col - 1] * powers[col] % (10**9 + 7)
                )

        answers = []
        for p, q in queries:
            answers.append(table[p][q])

        return answers