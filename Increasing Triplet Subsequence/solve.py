class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one,two = float('inf'),float('inf')
        
        for i in nums:
            if i <= one:
                one = i
            elif i <= two:
                two = i
            else: return True
        return False
        