class Solution :
    
    def mergeSort(self , head) :
        if not head or not head.next :
            if head : 
                head.prev = None
                head.next = None
            return head
        slow = fast = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        slow.prev.next = None
        slow.prev = None
        right = self.mergeSort(slow)
        left = self.mergeSort(head)
        dummy = Node(0)
        thead = dummy
        while left and right : 
            if left.data <= right.data :
                dummy.next = left
                left.prev = dummy
                left = left.next
            else :
                dummy.next = right
                right.prev = dummy
                right = right.next
            dummy = dummy.next
        if left :
            dummy.next = left
            left.prev = dummy
        if right :
            dummy.next = right
            right.prev = dummy
        ret_node = thead.next
        ret_node.prev = None
        thead.next = None
        return ret_node
    
    def sortDoubly(self,head):
        return self.mergeSort(head)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends