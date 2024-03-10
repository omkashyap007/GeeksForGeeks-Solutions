#User function Template for python3
class Solution:

	
	def removeDuplicates(self,string):
	    hash_map = {}
	    for i in string : 
	        hash_map[i] = hash_map.get(i,0)+1
	    answer = ""
	    for i in string : 
	        if hash_map[i] == -1 :
	            continue
	        answer += i
	        hash_map[i] = -1
	    return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends