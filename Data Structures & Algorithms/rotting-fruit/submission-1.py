class Solution:
    EMPTY = 'E'
    FRESH = 'F'
    ROTTEN = 'R'
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def orangesRotting(self, grid: List[List[int | str]]) -> int:
        # dfs with multi search, starting from rotten fruits. we need to find the banana with max distance, and fill in the grid. If some banana exists with 0/no path, then we return -1. Actually, even if one such banana exists, we can return -1.

        from collections import deque

        m = len(grid)
        n = len(grid[0])

        is_valid = lambda i, j: -1 < i < m and -1 < j < n and grid[i][j] == Solution.FRESH

        queue = deque()
        check_fresh = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    check_fresh.add((i, j))
                
                grid[i][j] = Solution.ROTTEN if grid[i][j] == 2 else \
                    (Solution.FRESH if grid[i][j] == 1 else Solution.EMPTY) 
        
        max_count = 0
        while queue:
            i, j = queue.popleft()
            for di, dj in Solution.DIRS:
                p, q = i + di, j + dj

                if is_valid(p, q):
                    grid[p][q] = (grid[i][j] + 1) if grid[i][j] != Solution.ROTTEN else 1

                    check_fresh.discard((p, q))
                    queue.append((p, q))
                    max_count = max(grid[p][q], max_count)
        
        return max_count if not check_fresh else -1

