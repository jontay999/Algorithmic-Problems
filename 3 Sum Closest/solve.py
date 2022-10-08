class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = float('inf')
        nums.sort()
        for i in range(len(nums)):
            newTarget = target - nums[i]
            j,k = i+1, len(nums)-1
            while j < k:
                res = newTarget - nums[j] - nums[k]
                if abs(res) < abs(best):
                    best = res

                # overshoot
                if res < 0:
                    k -= 1
                else:
                    j += 1
            
        return target - best
                
            