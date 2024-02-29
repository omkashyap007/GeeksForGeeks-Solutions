class Solution:

	def sumBitDifferences(self,arr, n):
	    answer = 0
	    for i in range(31):
	        totalOnes = 0
            for j in  range(n):
                if (arr[j]&(1<<i)) :
                    totalOnes += 1
            answer += (2*(totalOnes)*(n-totalOnes))
        return answer
	        
#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends