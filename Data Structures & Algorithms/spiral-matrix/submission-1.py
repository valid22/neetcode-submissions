class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        order = []

        while top <= bottom and left <= right:

            # → right
            for c in range(left, right + 1):
                order.append(matrix[top][c])
            top += 1

            # ↓ down
            for r in range(top, bottom + 1):
                order.append(matrix[r][right])
            right -= 1

            # ← left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    order.append(matrix[bottom][c])
                bottom -= 1

            # ↑ up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    order.append(matrix[r][left])
                left += 1

        return order