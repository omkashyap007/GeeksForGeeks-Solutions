
from typing import Optional
from collections import deque

class Solution:
    
    def inOrder(self , root):
        stack = []
        answer = []
        while root or stack : 
            if root :
                stack.append(root)
                root = root.left
            else :
                root = stack.pop()
                answer.append(root.data)
                root = root.right
        return answer
    
    def merge(self , left ,  right , arr , count):
        i = j = k = 0
        while i < len(left) and j < len(right) :
            if left[i] <= right[j] : 
                arr[k] = left[i]
                i += 1
                k += 1
            else :
                arr[k] = right[j]
                count[0] += len(left)-i
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
    
    def countInversions(self , arr, count):
        if len(arr) > 1 : 
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.countInversions(left , count)
            self.countInversions(right , count)
            self.merge(left , right , arr , count)
    
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        in_order = self.inOrder(root)
        count = [0]
        self.countInversions(in_order, count)
        return count[0]
        
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends