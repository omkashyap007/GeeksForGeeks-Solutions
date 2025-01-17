
from collections import deque

class Solution:
    
    def createAdjacencyList(self , V , edges ):
        adj_list = [[] for _ in range(V)]
        for second , first in edges :
            adj_list[first].append(second)
        return adj_list
        
    def topoSort(self , V , adj_list):
        indegree = [0 for _ in range(V)]
        for root in range(V):
            for node in adj_list[root]:
                indegree[node] += 1
        answer = []
        queue = deque([])
        for root in range(V):
            if indegree[root] == 0 : 
                queue.append(root)
        while queue : 
            root = queue.popleft()
            answer.append(root)
            for node in adj_list[root] :
                indegree[node] -= 1
                if indegree[node] == 0 :
                    queue.append(node)
        return answer
    
    def isPossible(self, n, m, p):
        adj_list = self.createAdjacencyList(n , p)
        answer = self.topoSort(n , adj_list)
        return [] if len(answer) != n else answer






#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
        print("~")
# } Driver Code Ends