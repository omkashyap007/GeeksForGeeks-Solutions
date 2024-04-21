#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        low = 0 
        high = n-1
        i = 0
        while i < len(arr) and i <= high :
            if arr[i] < 1 :
                arr[low] , arr[i] = arr[i] , arr[low] 
                low += 1
            if arr[i] > 1 :
                arr[high] , arr[i] = arr[i] , arr[high]
                high -= 1
                i -= 1
            i += 1
        return arr
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends