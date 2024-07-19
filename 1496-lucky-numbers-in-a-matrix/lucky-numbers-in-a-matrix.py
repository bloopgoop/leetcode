class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = []
        maxes = []
        for row in matrix:
            mins.append(min(row))
        
        for i in range(len(matrix[0])):
            col = [row[i] for row in matrix]
            maxes.append(max(col))

        res = []
        for m in mins:
            if m in maxes:
                res.append(m)
        return res