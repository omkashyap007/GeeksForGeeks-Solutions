#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class DSU:
    def __init__(self , n) :
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        
    def findParent(self , u):
        if self.parent[u] == u :
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent
        
    def union(self , u , v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        size_u = self.size[parent_u]
        size_v = self.size[parent_v]
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else : 
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
        
class Solution:
    def Solve(self, n, edges):
        dsu = DSU(n)
        cyclic_edges = 0
        for start , end in edges :
            if dsu.findParent(start) != dsu.findParent(end) :
                dsu.union(start , end)
            else : 
                cyclic_edges += 1 
        components = 0
        for i in range(n):
            if dsu.parent[i] == i :
                components += 1
        if cyclic_edges+1 < components :
            return -1
        return components -1
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends