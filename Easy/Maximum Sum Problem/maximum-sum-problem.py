class Solution:
    def maxSum(self, n):
        a = int(n/2)
        b = int(n/3)
        c = int(n/4)
        if (a+b+c) > n : 
            return self.maxSum(a) + self.maxSum(b) + self.maxSum(c) 
        return n



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends