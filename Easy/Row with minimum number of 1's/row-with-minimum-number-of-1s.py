#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        index = -1
        one_count = m+1
        for i in range(len(a)) :
            s = sum(a[i])
            if s < one_count :
                index = i+1
                one_count = s
        return index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends