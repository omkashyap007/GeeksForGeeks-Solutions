class Solution:
    def matrixDiagonally(self,mat):
        # code here
        self.n = len(mat)
        self.pattern = []
    
        # Flag to indicate upward or downward traversal
        upward = False
    
        for i in range(self.n):
            if upward:
                # Traverse upwards
                row, col = 0, i
                while col >= 0:
                    self.pattern.append(mat[row][col])
                    row += 1
                    col -= 1
                upward = False
            else:
                # Traverse downwards
                row, col = i, 0
                while row >= 0:
                    self.pattern.append(mat[row][col])
                    row -= 1
                    col += 1
                upward = True
    
        for i in range(1, self.n):
            if upward:
                # Traverse upwards
                row, col = i, self.n - 1
                while row < self.n:
                    self.pattern.append(mat[row][col])
                    row += 1
                    col -= 1
                upward = False
            else:
                # Traverse downwards
                row, col = self.n - 1, i
                while col < self.n:
                    self.pattern.append(mat[row][col])
                    row -= 1
                    col += 1
                upward = True
    
        return self.pattern

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends