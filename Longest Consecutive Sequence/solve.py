class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        best = 0
        for i in nums:
            if i in seen: continue
            seen.add(i)
            curr = i
            
            count_up = 0
            while curr + count_up + 1 in nums:
                count_up += 1
                seen.add(curr + count_up + 1)
            
            count_down = 0
            while curr - count_down - 1 in nums:
                count_down += 1
                seen.add(curr - count_down + 1)
            
            best = max(best, 1 + count_up + count_down)
        return best
        