class Solution:
    def twoRepeated(self, arr , n):
        answer = [] 
        for i in range(n+2) :
            element = abs(arr[i])
            index = element-1
            if arr[index] < 0 :
                answer.append(index+1)
            else :
                arr[index] = -1*arr[index]
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends