#User function Template for python3
class Solution:
	def NBitBinary(self, n):
	    answer = []
	    for i in range(1 , 1<<n) :
	        s = bin(i)[2:]
	        if len(s) != n : 
	            continue
	        ok = True
	        for j in range(1,len(s)+1):
	            a = s[:j]
	            if a.count("0") > a.count("1") :
	                ok = False
	        if ok : 
	            answer.append(s)
	    return answer[::-1]
	                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends