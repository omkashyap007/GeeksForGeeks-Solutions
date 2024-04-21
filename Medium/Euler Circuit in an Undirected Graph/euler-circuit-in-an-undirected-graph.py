class DSU : 
    def __init__(self , n):
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
        if parent_u == parent_v :
            return 0
        size_u = self.size[parent_u]
        size_v = self.size[parent_v]
        if size_v > size_u : 
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
        return 1

class Solution:
    def isEularCircuitExist(self, v, adj):
        edges = []
        for i in range(len(adj)):
            edges.extend([(i , j) for j in adj[i] if i < j ])
        if len(edges) == 0 : 
            return True
        dsu = DSU(v)
        for i in range(len(edges)):
            first = edges[i][0]
            second = edges[i][1]
            if dsu.findParent(first) == dsu.findParent(second):
                if i == len(adj) - 1 :
                    return True
                else :
                    return False
            else :
                dsu.union(first , second)
        return False





#{ 
 # Driver Code Starts
#Initial Template for python3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isEularCircuitExist(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends