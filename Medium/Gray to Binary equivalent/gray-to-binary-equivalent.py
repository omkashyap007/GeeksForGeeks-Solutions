#User function Template for python3

class Solution:
    def grayToBinary(self,n):
        answer = n
        while n>0 :
            n>>=1
            answer^=n
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends