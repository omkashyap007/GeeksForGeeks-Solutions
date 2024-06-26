class Solution:
    def deleteK(self, head, k):
        dummy = node(0)
        thead = dummy
        c = 0
        while head :
            c += 1
            if c == k :
                c = 0
            else :
                dummy.next = head
                dummy = dummy.next
            if head : 
                n = head.next 
                head.next = None
                head = n
            else :
                break
        return thead.next

#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends