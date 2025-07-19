class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def insertInMiddle(self, head, x):
        # If the list is empty, return a new node as the head
        if head is None:
            return Node(x)
        
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        # Move fast pointer two steps and slow pointer one step
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Create a new node
        newNode = Node(x)
        
        # Insert the new node after 'slow'
        newNode.next = slow.next
        slow.next = newNode
        
        return head
