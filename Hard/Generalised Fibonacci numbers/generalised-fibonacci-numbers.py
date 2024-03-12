class Solution:
    # Function to multiply two matrices
    def multiply_matrices(self, matrix1, matrix2, modulus):
        result = [[0, 0, 0] for _ in range(3)]  # Initialize the result matrix
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]  # Matrix multiplication
                result[i][j] %= modulus  # Apply modulus operation
        return result

    # Function to exponentiate a matrix
    def exponentiate_matrix(self, matrix, exponent, modulus):
        identity = [[(i == j) * 1 for j in range(3)] for i in range(3)]  # Identity matrix
        if exponent == 0:
            return identity  # If exponent is 0, return the identity matrix
        result = identity  # Initialize the result as the identity matrix
        base = matrix  # Initialize base matrix
        while exponent > 0:
            if exponent % 2 == 1:
                result = self.multiply_matrices(result, base, modulus)  # Multiply result by base if exponent is odd
            exponent //= 2  # Halve the exponent
            base = self.multiply_matrices(base, base, modulus)  # Square the base matrix
        return result

    # Function to generate Fibonacci number
    def genFibNum(self, a, b, c, n, modulus):
        if n <= 2:
            return 1 % modulus  # Return 1 if n is 1 or 2
        fib_matrix = [[a, b, c], [1, 0, 0], [0, 0, 1]]  # Fibonacci matrix
        result_matrix = self.exponentiate_matrix(fib_matrix, n - 2, modulus)  # Exponentiate the Fibonacci matrix
        return sum(result_matrix[0]) % modulus  # Return the sum of the first row of the result matrix

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends