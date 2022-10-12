class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        while i >= 2 and nums[i-1] + nums[i-2] <= nums[i]:
            i -= 1
        if i < 2:
            return 0
        return nums[i-1]+nums[i-2]+ nums[i]
            