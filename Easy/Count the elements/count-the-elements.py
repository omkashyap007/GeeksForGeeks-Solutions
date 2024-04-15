#User function Template for python3
class Solution:
    
    def searchElement(self , array , value) :
        l = 0
        r = len(array)-1
        while l <= r :
            mid = (l+r)//2
            if array[mid] <= value :
                l = mid + 1
            else : 
                r = mid-1
        return l
    
    def countElements(self, a, b, n, query, q):
        b.sort()
        answer = [-1 for _ in range(q)]
        for i in range(q)  :
            value = a[query[i]]
            answer[i] = self.searchElement(b,  value)
        return answer
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends