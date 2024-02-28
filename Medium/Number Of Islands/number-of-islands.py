from typing import List

class DSU:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        
    def findParent(self , u) :
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
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        answer = [0 for _ in range(len(operators))]
        dsu = DSU(rows*cols)
        count = 0
        dirs = [(0,1) , (1,0) ,(-1,0),(0,-1)]
        for i in range(len(operators)):
            row , col = operators[i]
            if visited[row][col] == 1 :
                answer[i] = count
            else : 
                visited[row][col] = 1
                count += 1
                for dx , dy in dirs :
                    x , y = row+dx , col+dy
                    if x>=0 and x<rows and y>=0 and y < cols and visited[x][y] == 1:
                        adj = x*cols + y
                        curr = row*cols + col
                        if dsu.findParent(curr) != dsu.findParent(adj):
                            dsu.union(curr , adj)
                            count -= 1
                answer[i] = count
        return answer
                
                
                
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends