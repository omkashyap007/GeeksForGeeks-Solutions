class Solution:
    def series(self, n):
        MOD = 10**9 + 7
        dp = [-1 for _ in range(n+1)]
        if n == 0 :
            return [0]
        if n == 1 : 
            return [0 ,  1]
        dp[0] = 0
        dp[1] = 1
        for i in range(2 , n+1):
            dp[i] = ((dp[i-1])%MOD + (dp[i-2] ) % MOD)%MOD
        return dp
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends