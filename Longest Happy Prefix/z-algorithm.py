def create_Zarr(string):
    string = string + "$" + string
    n = len(string)
    z = [0]* n
    left, right, k = 0, 0, 0
    for i in range(1, n):
        if i > right:
            left, right = i, i
            while right < n and string[right - left] == string[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < n and string[right - left] == string[right]:
                    right += 1
                z[i] = right - left
                right -= 1
    return z\

def getZArray(s):
    n = len(s)
    pattern = s + "$" + s
    Z_arr = [0] * len(pattern)


    left, right, k = 0,0,0
    #[Left, Right] represents the currently matched prefix
    for i in range(1, len(pattern)):
        # Case 1: It doesn't match any of the prefix so far
        if i > right:
            left, right = i,i
            while right < len(pattern) and pattern[right] == pattern[right - left]:
                right += 1
            # this amount of characters matched prefix
            Z_arr[i] = right - i
            # because the curr character was the mismatch of prefix
            right -= 1
        
        # Case 2: the current letter is within the prefix matched interval
        else:
            k = i- left
            if Z_arr[k] < right -i + 1:
                Z_arr[i] = Z_arr[k]
            else:
                left = i
                while right < len(pattern) and pattern[right] == pattern[right-left]:
                    right += 1
                
                Z_arr[i] = right - left
                right -= 1

    return Z_arr


s1 = "level"
s2 = "ababab"
assert getZArray(s1) == create_Zarr(s1), getZArray(s1)
assert getZArray(s2) == create_Zarr(s2), getZArray(s2)

print("passed")