class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        left = 0
        while left < len(colors):
            right = left + 1
            max_elem = neededTime[left]
            running_total = neededTime[left]
            while right < len(colors) and colors[right] == colors[left]:
                running_total += neededTime[right]
                max_elem = max(neededTime[right], max_elem)
                right += 1
            
            if right - left > 1:
                total += running_total - max_elem
            
            left = right
        
        return total
                
                