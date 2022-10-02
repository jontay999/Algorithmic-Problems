class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp[i][j] = number of ways to get j with i dice
        dp = [[0 for _ in range(target+1)] for i in range(n+1)]
        for i in range(1,min(k+1, target+1)):
            dp[1][i] = 1
        
        for i in range(1, min(target+1, n+1)):
            dp[i][i] = 1
        
        
        for i in range(2, n+1):
            for j in range(i+1, target+1):
                dp[i][j] = sum(dp[i-1][max(0, j - k): j]) % (10**9 + 7)
        
        return dp[-1][-1]