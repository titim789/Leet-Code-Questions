class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m != 0:
            n = len(obstacleGrid[0])
        else:
            return 0
        
        dp = [[False for i in range(n)] for j in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == m-1 and j == n-1:
                        dp[i][j] = 1
                    elif i == m-1:
                        dp[i][j] = dp[i][j+1]
                    elif j == n-1:
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]