class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                b = (i // 3) * 3 + (j // 3)

                if c != "." and (c in boxes[b] or c in rows[i] or c in cols[j]):
                    # print(f"Failed on {(i, j) = }, {c = } | {c in boxes[b] = } {c in rows[i] = } {c in cols[j] = }")
                    return False 
                
                boxes[b].add(c)
                rows[i].add(c)
                cols[j].add(c)

        return True