import heapq

class Solution:
    def spanningTree(self, V, adj_list):
        mst = []
        weight_sum = 0
        visited = [False for _ in range(V)]
        heap = [(0 , 0 , -1)]
        while heap :
            dist , root , parent = heapq.heappop(heap)
            if visited[root] :
                continue
            visited[root] = True
            if parent != -1 :
                mst.append((parent, root))
            weight_sum += dist
            for node , weight in adj_list[root] :
                if visited[node] :
                    continue
                heapq.heappush(heap , (weight , node ,  root))
        return weight_sum
            


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