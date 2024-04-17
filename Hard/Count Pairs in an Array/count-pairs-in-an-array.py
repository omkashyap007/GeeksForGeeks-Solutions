#User function Template for python3

class Solution:    
    def countPairs(self,arr, n):
        answer = 0
        for i in range(n) :
            arr[i] *= i
        def mergeSort(arr) :
            nonlocal answer
            if len(arr) > 1 :
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                mergeSort(left) 
                mergeSort(right)
                
                i = j = k = 0
                while i < len(left) and j < len(right) :
                    if left[i] <= right[j] :
                        arr[k] = left[i]
                        i += 1
                    else :
                        arr[k] = right[j]
                        answer += (len(left)-i)
                        j += 1
                    k += 1
                while i < len(left) :
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right) :
                    arr[k] = right[j]
                    j += 1
                    k += 1
            return 
        mergeSort(arr)
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends