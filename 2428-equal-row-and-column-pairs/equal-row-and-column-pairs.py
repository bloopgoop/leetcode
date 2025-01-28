class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0

        row_count = {}
        for row in grid:
            if str(row) not in row_count:
                row_count[str(row)] = 1
            else:
                row_count[str(row)] += 1
        
        for i in range(len(grid)):
            col = [grid[j][i] for j in range(len(grid))]
            if str(col) in row_count:
                res += row_count[str(col)]

        return res