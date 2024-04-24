class Solution:
    def ways(self, n,m):
        n += 1
        m += 1
        dp =  [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        MOD = 10**9 + 7
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0 :
                    continue
                top = dp[i-1][j] if i-1 >= 0 else 0
                down = dp[i][j-1] if j-1 >=0 else 0
                dp[i][j] = (top + down ) %MOD
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    x,y=list(map(int,input().split()))
    ob = Solution()
    print(ob.ways(x,y))
# } Driver Code Ends