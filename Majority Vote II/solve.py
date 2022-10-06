class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1,c2,n1,n2 = 0,0, None, None
        
        for i in nums:
            if n1 == i:
                c1 += 1
            elif n2 == i:
                c2 += 1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 == 0:
                n2 = i
                c2 = 1
            else:
                c2 -= 1
                c1 -= 1
        
        c3, c4 = 0,0
        for i in nums:
            if i == n1:
                c3 += 1
            elif i == n2:
                c4 += 1
        res = []
        if c3 > len(nums)//3:
            res.append(n1)
        if c4 > len(nums)//3:
            res.append(n2)
        
        return res
            