class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid) - 1
        n = len(grid[0]) - 1

        for i in range(1,n+1):
            grid[0][i] += grid[0][i-1]

        for i in range(1,m+1):
            grid[i][0] += grid[i-1][0]
        
        # [print(x) for x in grid]

        for i in range(1,m+1):
            for j in range(1,n+1):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        # [print(x) for x in grid]
        return grid[m][n]