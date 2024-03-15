#User function Template for python3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def merge_sorted(self,h1,h2):
        res=Node(None)
        curr=res
        while h1 and h2:
            if h1.data<h2.data:
                curr.next=h1
                curr=h1
                h1=h1.next
            else:
                curr.next=h2
                curr=h2
                h2=h2.next
        if h1:
            curr.next=h1
        if h2:
            curr.next=h2
        return res.next
    
    def sort(self, h1):
        curr=h1
        desc=None
        while curr and curr.next:
            temp=desc
            desc=curr.next
            temp2=desc.next
            desc.next=temp
            curr.next=temp2
            curr=curr.next
        h1=self.merge_sorted(h1,desc)
        return h1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends