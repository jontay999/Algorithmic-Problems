"Given an array of integers with an alphabet mapping from A-J, produce a mapping that minimizes the sum"

from numpy import argsort
def minSum(array):
    #Initialise Matrix
    #row[i] = 10^i
    #col[j] = chr(ord('A') + j)
    matrix = [[0 for _ in range(10)] for i in range(10)]
    rows, cols = 10,10

    # Set up checks
    no_zeros = set()
    char_set = set()

    # Populate values
    for num in array:
        if not num[0].isdigit():
            no_zeros.add(num[0])
        for i in range(len(num)):
            power = len(num) -i -1
            if not num[i].isdigit():
                char_set.add(num[i])
                matrix[power][ord(num[i]) - ord('A')] += 1
    
    # Carry values down
    for i in range(rows-1):
        for j in range(cols):
            quotient, remainder = divmod(matrix[i][j], 10)
            matrix[i][j] = remainder
            matrix[i+1][j] += 1


    #mapping
    d = {}

    #Find the num with zero
    if len(char_set) != no_zeros:
        currRow = rows-1
        bestIdx = None
        bestCount = 0
        while currRow >= 0 and bestIdx == None:
            for j in range(cols):
                if chr(ord('A') + j) in no_zeros: continue
                if matrix[currRow][j] > bestCount:
                    bestIdx = j 
                    bestCount = matrix[currRow][j]
            if bestIdx == None:
                currRow -= 1
            else:
                d[chr(ord('A') + j)] = 0
    sums = [0] *10
    for i in range(rows):
        for j in range(cols):
            sums[j] += matrix[i][j] * (10**i)
    
    sumIdxSort = argsort(sums)
    for idx,i in enumerate(sumIdxSort):
        d[chr(ord('A') + i)] = idx+1
    
    total = 0
    for num in arr:
        new_num = list(num)
        for i in range(len(new_num)):
            if new_num[i] in d:
                new_num[i] = d[new_num[i]]
        new_num = int(''.join(list(map(int, new_num))))
        total += new_num
    return total


        

        