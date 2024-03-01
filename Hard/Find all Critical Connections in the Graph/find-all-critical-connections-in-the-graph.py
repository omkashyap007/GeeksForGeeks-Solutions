class Solution:

    time = 0

    def dfs(self , root , parent , lowest_time , insertion_time , visited , adj_list , bridges):
        visited[root] = True
        insertion_time[root] = lowest_time[root] = self.time
        self.time += 1
        for node in adj_list[root] :
            if node == parent :
                continue
            if visited[node] :
                lowest_time[root] = min(lowest_time[root] , lowest_time[node])
            else :
                self.dfs(node , root , lowest_time , insertion_time , visited ,adj_list , bridges)
                lowest_time[root] = min(lowest_time[root] , lowest_time[node])
                if insertion_time[root] < lowest_time[node] :
                    if root > node :
                        bridges.append((node,root))
                    else : 
                        bridges.append((root , node))
                

    def criticalConnections(self, v, adj_list):
        visited = [False for _ in range(v)]
        lowest_time = [0 for _ in range(v)]
        insertion_time = [0 for _ in range(v)]
        bridges = []
        self.dfs(0 , -1 , lowest_time , insertion_time , visited , adj_list , bridges)
        return sorted(bridges)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends