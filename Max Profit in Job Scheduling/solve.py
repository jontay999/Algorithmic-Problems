# DP with binary search

# Time: O(n log n)
# Space: O(n)

import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(endTime, startTime, profit))
        arr.sort()
        time = [0,arr[0][0]]
        dp = [0,arr[0][2]]
        
        n = len(arr)
        for i in range(1,n):
            end, start, val = arr[i] 
            
            # find insertion point of start time
            idx = bisect.bisect_right(time, start)-1
            
            if time[-1] == end:
                # if ending time the same, take the better one
                dp[-1] = max(dp[idx] + val, dp[-1])
            else:
                # # either take this job or don't take this job
                best = max(dp[idx] + val, dp[-1])
                dp.append(best)
                time.append(end)
        return dp[-1]
            
        
        