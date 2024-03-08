#User function Template for python3
class Solution:
    def sameFreq(self, s):
        a = [0 for _ in  range(26)]
        for i in s :
            a[ord(i)-ord("a")] += 1
        n = [i for i in a if i != 0 ]
        if len(n) == 1 :
            return True
        a = min(n)
        s = len(n)*a
        ts = sum(n)
        if abs(s-ts) <= 1 :
            return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends