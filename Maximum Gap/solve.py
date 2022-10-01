class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        def countingSort(arr, digit):
            n = len(arr)
            counts = [0]*10
            idxs = [(i//(10**digit))%10 for i in arr]
            
            for i in range(n):
                counts[idxs[i]] += 1
            
            for i in range(1, 10):
                counts[i] += counts[i-1]
            for i in range(9,0,-1):
                counts[i] = counts[i-1]
            counts[0] = 0
            
            
            new_arr = [None]* n
            for i in range(n):
                new_arr[counts[idxs[i]]] = arr[i]
                counts[idxs[i]] += 1
            
            return new_arr
        
        max_digits = len(str(max(nums)))
        for i in range(max_digits):
            nums = countingSort(nums, i)
        
        best = float('-inf')
        for i in range(1, len(nums)):
            best= max(best, nums[i] - nums[i-1])
        return best
            
        