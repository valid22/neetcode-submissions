class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        first_row = any(matrix[0][c] == 0 for c in range(n))
        first_col = any(matrix[r][0] == 0 for r in range(m))

        # Mark rows and columns
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero based on markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first row
        if first_row:
            for c in range(n):
                matrix[0][c] = 0

        # Handle first column
        if first_col:
            for r in range(m):
                matrix[r][0] = 0