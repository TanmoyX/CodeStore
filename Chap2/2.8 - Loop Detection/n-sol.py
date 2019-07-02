class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def printLL(node):
    while node != None:
        print(node.data)
        node = node.next

def insertNode(node, val):
    if node == None:
        node = Node(val)
        return node 
    head = node
    while node.next != None:
        node = node.next
    node.next = Node(val)
    node.next.next = None
    return head

def detectLoop(node):
    slow = node
    fast = node
    meet = node
    
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if (fast != None and fast.next != None):
        while meet != slow:
            meet = meet.next
            slow = slow.next
        print(slow.data)

n = None
n = insertNode(n, 6)
n = insertNode(n, 4)
n = insertNode(n, 3)
n = insertNode(n, 5)

#Creating loop
n.next.next.next = n

detectLoop(n)