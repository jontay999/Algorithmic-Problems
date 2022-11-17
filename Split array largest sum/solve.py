# naiive solution O(kn^2)
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1: return sum(nums)
        d = {}
        
        best = float('inf')
        
        def dfs(i,k, currMax):
            nonlocal best
            if currMax >= best: return float('inf')
            
            key = (i,k)
            # not much point in checking this answer further
            if key in d and currMax > d[key]:
                return float('inf')
            
            # not enough for groupings
            if k > len(nums) - i: return float('inf')
            if k == 1:
                return max(currMax, sum(nums[i:]))
            
            bestRes = float('inf')
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                res = dfs(j+1, k-1, max(currSum, currMax))
                bestRes = min(res, bestRes)
                best = min(res, best)
                
            d[key] = bestRes
            return bestRes

        return dfs(0,k,0)


# binary search largest sum, O(n log (n*10^6))
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1: return sum(nums)
        
        def feasibleSum(largest):
            count = 0
            curr = 0
            for num in nums:
                curr += num
                if curr > largest:
                    count += 1
                    if count >= k: return False
                    curr = num
            return True

        l,r = max(nums), sum(nums)
        res = 0
        while l <= r:
            mid = (l+r)//2
            if feasibleSum(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        
        return res
                
            