class Solution:
    def inversionCount(self, arr, n):
        count = 0
        def mergeSortCount(arr):
            nonlocal count
            if len(arr) > 1 :
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                mergeSortCount(left)
                mergeSortCount(right)
                i = j = k = 0
                while i < len(left) and j < len(right) :
                    if left[i] <= right[j] : 
                        arr[k] = left[i]
                        i += 1
                        k += 1
                    else :
                        count += len(left)-i
                        arr[k] = right[j]
                        j += 1
                        k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k +=1 
                while j < len(right):
                    arr[k] = right[j]
                    j += 1 
                    k += 1
        mergeSortCount(arr)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends