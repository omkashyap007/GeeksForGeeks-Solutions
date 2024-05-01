class Solution:
    def arrangeCV(self, head):
        vowels = Node(0)
        v = vowels
        consonants = Node(0)
        c = consonants
        the_vowels = "aeiou"
        while head : 
            if head.data in the_vowels :
                vowels.next = head
                vowels = vowels.next
            else :
                consonants.next = head
                consonants = consonants.next
            head = head.next
        vowels.next = c.next
        consonants.next = None
        return v.next
        

#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends