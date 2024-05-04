class Solution:
    def buildTree(self , inorder, postorder, n):
        if not inorder :
            return None
        if len(inorder) ==1 :
            return Node(inorder[0])
        root_data = postorder[-1]
        i = 0
        while i < len(inorder) and inorder[i] != root_data :
            i += 1
        inorder_left = inorder[:i]
        inorder_right = inorder[i+1:]
        root = Node(root_data)
        if not inorder_right :
            postorder_right = []
            postorder_left = postorder[:-1]
        else :
            right_node_data = inorder[i+1]
            i = 0
            while i < len(postorder) and postorder[i] != right_node_data :
                i += 1
            postorder_left = postorder[:i]
            postorder_right = postorder[i:-1]
        root.left = self.buildTree(inorder_left , postorder_left , 0)
        root.right = self.buildTree(inorder_right , postorder_right , 0)
        return root
            
             
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import  defaultdict

#Contributed by : PranchalK


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())



# Helper function that allocates  
# a new node  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This funtcion is here just to test  
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        in_order = list(map(int, input().strip().split()))  # parent child info in list
        post_order = list(map(int, input().strip().split()))  # parent child info in list
        ob = Solution()
        preOrder(ob.buildTree(in_order,post_order,n))
        print()


# } Driver Code Ends