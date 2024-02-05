class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[False if i!=0 and j != 0 else 1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp [i][j-1]
        return dp[m-1][n-1]
        

        