def getRunLengthEncoding(string):
    res = []
    char = None
    idx = -1
    for i in range(len(string)):
        if char == None:
            char = string[i]
            res.append(char)
            idx = i
        elif string[i] != char:
            if i-idx > 1:
                res.append(i-idx)    
            char = string[i]
            idx = i
            res.append(char)
    if len(string)-idx > 1:
        res.append(len(string) - idx)
    
    return "".join(list(map(str, res)))
