#User function Template for python3

class Solution:
    
    def dfs(self , index , values , weights , W , cache ) :
        if (index , W) in cache : 
            return cache[(index,W)]
        if index == 0 :
            if weights[index] <= W :
                return values[index]
            return 0
        take = 0
        if weights[index] <= W :
            take = self.dfs(index-1 , values , weights , W-weights[index] , cache) + values[index]
        not_take = self.dfs(index-1 , values , weights ,  W , cache)
        cache[(index,W)] = max(take , not_take)
        return max(take ,  not_take)
    
    def knapSack(self,W, wt, val, n):
        cache = {}
        return self.dfs(n-1 ,val ,  wt ,  W , cache )


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
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends