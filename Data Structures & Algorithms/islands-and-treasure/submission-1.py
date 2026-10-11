class Solution:
    INF = 2147483647
    WATER = -1
    CHEST = 0
        
    def bfs_search(self, grid):
            from collections import deque
    
            if not grid or not grid[0]:
                return
            
            m, n = len(grid), len(grid[0])
            is_valid = lambda i, j: -1 < i < m and -1 < j < n and grid[i][j] == Solution.INF
    
            queue: deque[tuple[int, int]] = deque()
            # visited: set[tuple[int, int]] =set()

            # find all chests/starting pos
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == Solution.CHEST:
                        queue.append((i, j)) # (row, col)
                        # visited.add((i, j))

            # down, up, right, left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
            while queue:
                p, q = queue.popleft()
                
                for (i, j) in directions:
                    x, y = p + i, q + j
                    if is_valid(x, y):
                        grid[x][y] = grid[p][q] + 1 # mark distance from nearest chest

                        
                        # visited.add((x, y))
                        queue.append((x, y))

            return grid
            

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.bfs_search(grid)
        
