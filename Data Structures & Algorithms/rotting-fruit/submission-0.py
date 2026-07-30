class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        q = deque()

        fresh = 0
        mins = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh > 0:
            for n in range(len(q)):
                row, col = q.popleft()

                for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        q.append([nr, nc])
                        fresh -= 1
                        grid[nr][nc] = 2
            mins += 1

        if fresh == 0:
            return mins
        else:
            return -1