class Solution:
    def longestPrefix(self, s: str) -> str:
        original_length = len(s)
        pattern = s + "$" + s
        n = len(pattern)
        Z_arr = [0] * n
        left, right = 0,0
        for i in range(1, n):
            if i > right:
                left, right = i,i
                while right < n and pattern[right] == pattern[right-left]:
                    right += 1
                Z_arr[i] = right - left
                right -= 1
            else:
                k = i - left
                if Z_arr[k] < right - i + 1:
                    Z_arr[i] = Z_arr[k]
                else:
                    left = i
                    while right < n and pattern[right] == pattern[right-left]:
                        right += 1
                    Z_arr[i] = right - left
                    right -= 1
        
        bestIdx = -1
        for i in range(original_length-1):
            if Z_arr[-i-1] == i+1:
                bestIdx = i

        if bestIdx == -1:
            return ""
        return s[:bestIdx+1]
        
                
                
        