class Solution:
	def shortest_distance(self, matrix):
	    for i in range(len(matrix)):
	        for j in range(len(matrix)):
	            if matrix[i][j] == -1 :
	                matrix[i][j] = float("inf")
	    for via in range(len(matrix)):
	        for i in range(len(matrix)):
	            for j in range(len(matrix)):
	                matrix[i][j] = min(matrix[i][j] , matrix[i][via] + matrix[via][j])
	    for i in range(len(matrix)):
	        for j in range(len(matrix)) :
	            if matrix[i][j] == float("inf") :
	                matrix[i][j] = -1
	    return matrix
    

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends