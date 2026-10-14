class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        while r < len(matrix):
            if matrix[r][0] > target:
                break
            
            r += 1
        
        r -= 1
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                return True

        return False