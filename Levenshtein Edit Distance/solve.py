def edit_distance(x, y):
    """
    Return the number of insertions, deletions and substitutions required to transform x into y.
    x and y are two strings. Use the matrix approach here.

    x: The first word.
    y: The second word.
    Return value: The number of insertions, deletions and substitutions to transform the first
    word into the second word.
    """
    matrix = [[0 for _ in range(len(y)+1)] for i in range(len(x)+1)]

    for i in range(1,len(y)+1):
        matrix[0][i] = i
    for i in range(1, len(x)+1):
        matrix[i][0] = i
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
    return matrix[-1][-1]