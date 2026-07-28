class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0" or grid[row][col] == "#":
                return

            grid[row][col] = "#"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count