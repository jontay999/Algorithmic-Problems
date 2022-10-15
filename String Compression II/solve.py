
# Fairly slow, 5%
def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    @cache
    def dfs(idx, char, length, remaining):
        if char == None:
            chain_length = 0
        if length == 1:
            chain_length = 1
        else:
            chain_length = len(str(length)) + 1
        
        if idx == len(s): return chain_length

        possible = []
        if s[idx] == char:
            keep = dfs(idx+1, char, length+1, remaining)
            possible.append(keep)
            if remaining > 0:
                dont_keep = dfs(idx+1, char, length, remaining-1)
                possible.append(dont_keep)
        elif s[idx] != char:
            if remaining > 0:
                dont_keep = dfs(idx+1, char, length, remaining-1)
                possible.append(dont_keep)
                
            keep = dfs(idx+1, s[idx], 1, remaining) + chain_length
            possible.append(keep)
        # print(f"idx: {idx}, char: {char}, length: {length}, remaining: {remaining}, possible:", possible)
        return min(possible)
    
    return dfs(0,None, 0, k)-2
    
    
    
# More optimal O(kn^2)

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        n = len(s)
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        #dp[i][j] best solution up to s[i] with at most j removals
        
        
        for i in range(k+1):
            dp[0][i] = 0
        
        for i in range(1, n+1):
            for j in range(k+1):
                # start with trying to remove the current character
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]
                
                # keep this current character
                chain_length = 0
                removed = 0
                # try to keep removing up to j characters before 
                for m in range(i,0,-1):
                    # same character, increase chain length
                    if s[m-1] == s[i-1]:
                        chain_length += 1
                    else:
                        # have to remove
                        removed += 1
                        if removed > j:
                            break
                    
                    if chain_length == 1:
                        real_length = 1
                    else:
                        real_length = len(str(chain_length)) + 1
                    
                    # check if the answer to previous substring with the remaining removals + chain length is optimal
                    dp[i][j] = min(dp[i][j], dp[m-1][j - removed] + real_length)

        return dp[-1][-1]

