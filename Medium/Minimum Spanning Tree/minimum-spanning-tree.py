class DSU:
    
    def __init__(self , n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
        
    def findParent(self , u):
        if self.parent[u] == u : 
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent
        
    def union(self , u , v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        size_u = self.size[u]
        size_v = self.size[v]
        
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
            self.parent[u] = self.findParent(v)
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
            self.parent[v] = self.findParent(u)

class Solution:
    def spanningTree(self, V, adj):
        edges = []
        for i in range(V):
            l = adj[i]
            for j in l:
                node = j[0]
                dist = j[1]
                edges.append((i , node , dist))
        min_sum = 0
        edges.sort(key = lambda x : x[2])
        min_sum = 0 
        dsu = DSU(V)
        for  start , end , dist in edges :
            if dsu.findParent(start) != dsu.findParent(end) :
                min_sum += dist
                dsu.union(start , end)
        return min_sum
    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends