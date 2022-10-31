# Time complexity = O(V^3)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = [[float('inf') for _ in range(n)] for i in range(n)]
        for i in range(n):
            graph[i][i] = 0

        for u,v,weight in edges:
            graph[u][v] = weight
            graph[v][u] = weight
        
        for i in range(n):
            # i means using ith vertex as intermediate
            for j in range(n):
                if j == i: continue
                for k in range(n):
                    if i == k or j == k: continue
                    #j,k means the pair of j->i and i -> k
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
        
        best_city_count = float('inf')
        idx = -1
        for i in range(n):
            city_count = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    city_count += 1
            if city_count <= best_city_count:
                best_city_count = city_count
                idx = i
        return idx
                
                