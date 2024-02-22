from collections import deque
from typing import List
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        MOD = 100000
        min_steps = float("inf")
        distances = [float("inf") for _ in range(MOD)]
        queue = deque([(0 , start)])
        while queue : 
            steps , root = queue.popleft()
            if root == end : 
                return steps
            for node in arr :
                new_number = (root * node ) %MOD
                if steps +1 < distances[new_number] :
                    queue.append((steps+1 , new_number))
                    distances[new_number] = steps+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends