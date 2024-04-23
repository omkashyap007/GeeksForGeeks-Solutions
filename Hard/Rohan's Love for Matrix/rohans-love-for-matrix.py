#User function Template for python3
class Solution:
    def firstElement (self, n):
        MOD = 10**9+7
        a , b = 0 , 1
        if n  < 2 :return n
        for i in range(n):
            a , b = b%MOD , (a+b)%MOD
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends