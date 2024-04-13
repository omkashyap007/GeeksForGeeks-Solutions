#User function Template for python3

class Solution:
    def reversedBits(self, x):
        a = bin(x)[2:]
        a = "0"*(32-len(a))+a
        answer = 0
        for i in range(31,-1,-1):
            if a[i] == "1" :
                answer += (1<<i)
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends