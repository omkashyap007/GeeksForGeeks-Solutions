class Solution:
    MAX = float("inf")
    def bellman_ford(self, V, edges, source ):
        distances = [self.MAX for _ in range(V)]
        distances[source] = 0
        for _ in range(V-1):
            for root , node , node_distance in edges:
                if distances[root] + node_distance < distances[node] :
                    distances[node] = distances[root] + node_distance
        updated = False
        for root , node , node_distance in edges:
            if distances[root] + node_distance < distances[node] :
                updated = True
                break
        if not updated :
            return list(map(lambda x : 10**8 if x == float("inf") else x , distances))
        return [-1]
        
        

        

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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends