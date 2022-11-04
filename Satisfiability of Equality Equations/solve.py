class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        
        
        mapping = {}
        count = 0
        for i in range(n):
            if equations[i][0] not in mapping:
                mapping[equations[i][0]] = count
                count += 1
            if equations[i][-1] not in mapping:
                mapping[equations[i][-1]] = count
                count += 1
        
        parents = [i for i in range(count)]
        rank = [1 for i in range(count)]
        
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
        
    
        
        for i in range(n):
            if equations[i][1] == "=":
                union(mapping[equations[i][0]], mapping[equations[i][-1]])
        
        for i in range(n):
            if equations[i][1] == "!":
                if find(mapping[equations[i][0]]) == find(mapping[equations[i][-1]]):
                    return False
        return True