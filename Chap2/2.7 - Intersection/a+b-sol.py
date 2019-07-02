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

def getLength(node):
    length = 0
    head = node
    while head != None:
        length += 1
        head = head.next
    return length

def intersection(n1, n2):
    head1 = n1
    head2 = n2
    len1 = getLength(n1)
    len2 = getLength(n2)
    
    if len1 > len2:
        gap = len1 - len2
        while gap > 0:
            head1 = head1.next
            gap -= 1
    else:
        gap = len2 - len1
        while gap > 0:
            head2 = head2.next
    while head1 != head2:
        if head1 == head2:
            print(head1.data)
        head1 = head1.next
        head2 = head2.next
    print(head1.data)
    
n1 = None
n1 = insertNode(n1, 6)
n1 = insertNode(n1, 4)
n1 = insertNode(n1, 9)
n1 = insertNode(n1, 3)
n1 = insertNode(n1, 4)
n1 = insertNode(n1, 6)
printLL(n1)
print()

n2 = None
n2 = insertNode(n2, 1)
n2 = insertNode(n2, 2)
n2.next.next = n1.next.next
printLL(n2)
print()

intersection(n1, n2)