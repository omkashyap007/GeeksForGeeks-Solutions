#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        string = ""
        x = n
        while r > 0 :
            x = x//2 + 1
            for i in range(x):
                string += "01" if s[i] == "0" else  "10"
            s = string
            x = len(s)
            string = ""
            r -= 1
        return s[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends