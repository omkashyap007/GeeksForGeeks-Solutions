#User function Template for python3

class Solution:
    
    def findCombinations(self , index , array , string , answer):
        if index >= len(string) :
            if not array : 
                return 
            answer.append("".join(array))
            return
        array.append(string[index])
        self.findCombinations(index+1 , array , string , answer)
        array.pop()
        self.findCombinations(index+1 , array , string , answer)
        
    
	def AllPossibleStrings(self, s):
	    answer = []
        self.findCombinations(0 , [] , s , answer)
        answer.sort()
        return answer

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends