
class Solution:
    
    def max_Books(self, n, k, nums):
        answer = 0
        size = 0
        for r in range(n) :
            if nums[r] <= k :
                size += nums[r]
                answer = max(answer , size)
            else :
                size = 0
        return answer


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends