import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,heap,n) :
        answer = 0
        heapq.heapify(heap)
        while heap :
            if len(heap) == 1 :
                break
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            answer += (first+second)
            heapq.heappush(heap , first+second)
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minCost(a,n))
# } Driver Code Ends