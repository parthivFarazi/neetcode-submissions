# Pattern: DFS flooding

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    dfs(nr, nc)

            return

        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count


# O(m * n) time and space
# 6 mins 50 secs