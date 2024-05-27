
from typing import List


class Solution:
    def longestSubseq(self, n : int, nums : List[int]) -> int:
        dp = [1 for _ in range(n)]
        answer = 0 
        for i in range(1,n):
            for j in range(0 , i) :
                if abs(nums[i] - nums[j]) == 1 :
                    dp[i] = max( dp[i] , dp[j] + 1 )
                    answer = max(answer ,  dp[i])
        return answer
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.longestSubseq(n, a)

        print(res)

# } Driver Code Ends