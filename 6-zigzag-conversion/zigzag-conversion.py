class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = {}
        for row in range(numRows):
            rows[row] = []

        c = 0
        climb = True
        for char in s:
            rows[c].append(char)

            if c == 0:
                climb = True
            if c == numRows - 1:
                climb = False

            if climb:
                c += 1
            else:
                c -= 1

        res = ""
        for row in rows:
            res += "".join(rows[row])

        return res