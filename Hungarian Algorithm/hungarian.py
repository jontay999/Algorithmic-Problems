
# Python implementation and adapted from https://github.com/mpfeifer1/Kattis/blob/master/cordonbleu.cpp

# matrix[i][j] is cost of job i done by worker j
def hungarianMatch(matrix, minimize=True):
    # ensure that rows always <= cols
    if len(matrix) > len(matrix[0]):
        # transpose matrix
        matrix = list(map(list, zip(*matrix)))
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # flip weights if want to get maximum matching
    if not minimize:
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] *= -1

    u = [0 for _ in range(rows+1)]
    v = [0 for _ in range(cols+1)]
    p = [0 for _ in range(cols+1)]
    way = [0 for _ in range(cols+1)]
    for i in range(1,rows+1):

        p[0] = i 

        # minv is a labelling of a col nodes
        minv = [float('inf') for _ in range(cols+1)]
        used = [False for _ in range(cols+1)]

        j0 = 0

        while True:
            used[j0] = True
            
            i0 = p[j0]
            delta = float('inf')
            j1 = None

            for j in range(1,cols+1):

                # If col[j] has not been paired jp
                if not used[j]:
                    # do a  labelling, edge weight - label of row - label of col
                    cur = matrix[i0-1][j-1] - u[i0] - v[j]
                    
                    # minv is the curr labelling of the col[v] coming from row[i], update the labelling of minv if it is better
                    if cur < minv[j]:
                        minv[j] = cur 
                        way[j] = j0
                    
                    # im guessing that delta is the slack that you can push through the row[i] node and is limited by min[v]
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            
            for j in range(cols+1):
                if used[j]:
                    u[p[j]] += delta 
                    v[j] -= delta 
                else:
                    minv[j] -= delta 
            
            j0 = j1

            if p[j0] == 0: break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if not j0:
                break
    

    # // For each N, it contains the M it selected
    # vector<ll> ans(n+1);
    # for(ll j = 1; j <= m ; ++j)
    #     ans[p[j]] = j;

    
    if not minimize: return v[0]
    return -v[0]


arr = [[15,96],[36,2]]
hungarianMatch(arr)

