import heapq

class Solution:
    def dijkstra(self, V, adj_list, source):
        distances = [float("inf") for _ in range(V)]
        heap = [(0,source)]
        visited = [False for _ in range(V)]
        distances[source] = 0
        while heap :
            root_distance , root = heapq.heappop(heap)
            if visited[root] :
                continue
            for node , node_distance in adj_list[root] :
                if root_distance + node_distance < distances[node] :
                    distances[node] = root_distance + node_distance
                    heapq.heappush(heap , (root_distance + node_distance , node))
            visited[root] = True
        return distances    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends