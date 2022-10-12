# O(W * n) space complexity
def solve_knapsack(W, w, v):
    """
    Solve the knapsack with repetition problem.
    W is the total weight that the knapsack can carry.
    w[1...n] is a list that contains the weights of items.
    v[1...n] is a list that contains the values of items.
    """

    dp = [[0 for _ in range(W+1)] for i in range(len(w)+1)]
    
    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            # if current weight cannot choose the current item, is as good as looking on top
            if j < w[i-1]:
                space_dp[i][j] = space_dp[(i-1)][j]
            else:
                space_dp[i][j] = max(space_dp[(i-1)][j], space_dp[(i-1)][j - w[i-1]] + v[i-1])
    
    return max(map(max, space_dp))


# O(W) space complexity
def solve_knapsack_space_optimized(W, w, v):
    """
    Solve the knapsack with repetition problem.
    W is the total weight that the knapsack can carry.
    w[1...n] is a list that contains the weights of items.
    v[1...n] is a list that contains the values of items.
    """

    # Space optimized version
    space_dp = [[0 for _ in range(W+1)] for i in range(2)]
    
    for i in range(1, len(w)+1):
        row = i % 2
        for j in range(1, W+1):
            # if current weight cannot choose the current item, is as good as looking on top
            if j < w[i-1]:
                space_dp[row][j] = space_dp[(row-1) % 2][j]
            else:
                space_dp[row][j] = max(space_dp[(row-1) % 2][j], space_dp[(row-1) % 2][j - w[i-1]] + v[i-1])
    
    return max(map(max, space_dp))