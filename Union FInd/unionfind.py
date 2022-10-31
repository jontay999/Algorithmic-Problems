# Union find with path compression

parents = [i for i in range(n)]
rank = [1 for i in range(n)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    parentX = find(x)
    parentY = find(y)
    if rank[parentX] > rank[parentY]:
        parents[parentY] = parentX
    else:
        parents[parentX] = parentY
        if rank[parentX] == rank[parentY]:
            rank[parentY] += 1
