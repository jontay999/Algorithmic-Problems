# Problem
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        rows = len(cost)
        cols = len(cost[0])
        Lmin = [0 for _ in range(rows)]
        Rmin = [0 for _ in range(cols)]

        ans = 0
        for i in range(rows):
            Lmin[i] = float('inf')
            for j in range(cols):
                Lmin[i] = min(Lmin[i], cost[i][j])
            ans += Lmin[i]
        
        for j in range(cols):
            Rmin[j] = float('inf')
            for i in range(rows):
                Rmin[j] = min(Rmin[j], cost[i][j])
            ans += Rmin[j]
        
        for i in range(rows):
            for j in range(cols):
                cost[i][j] = max(-1*(cost[i][j] - Lmin[i] - Rmin[j]), 0)
                

        res = hungarianMatch(cost, False)
        return ans - res



# matrix[i][j] is cost of job i done by worker j
def hungarianMatch(matrix, minimize=True):
    
    # ensure that rows always <= cols
    if len(matrix) > len(matrix[0]):
        matrix = list(map(list, zip(*matrix)))
    
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # flip weights if 
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

        minv = [float('inf') for _ in range(cols+1)]
        used = [False for _ in range(cols+1)]

        j0 = 0

        while True:
            used[j0] = True
            
            i0 = p[j0]
            delta = float('inf')
            j1 = None

            for j in range(1,cols+1):
                if not used[j]:
                    cur = matrix[i0-1][j-1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur 
                        way[j] = j0
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
    
    if not minimize: return v[0]
    return -v[0]

