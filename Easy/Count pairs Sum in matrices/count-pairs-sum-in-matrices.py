class Solution : 
    def front(self,n,i,j):
        if j==n-1:
            i+=1
            j=0
        else:
            j+=1
        return i,j
    
    def rear(self,n,i,j):
        if j==0:
            i-=1
            j=n-1
        else:
            j-=1
        return i,j
    
    
    def is_valid(self,n,i,j,a,b):
        if i==n:
            return False
        if a==-1:
            return False
        return True
    
    def countPairs(self, mat1, mat2, n, x):
        i,j,a,b=0,0,n-1,n-1
        count=0
        while self.is_valid(n,i,j,a,b):
            sum=mat1[i][j]+mat2[a][b]
            if sum==x:
                count+=1
                i,j=self.front(n,i,j)
                a,b=self.rear(n,a,b)
            elif sum>x:
                a,b=self.rear(n,a,b)
            else:
                i,j=self.front(n,i,j)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends