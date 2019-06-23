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
        return None
    while node.next != None:
        node = node.next
    node.next = Node(val)
    node.next.next = None

def kthToLast(node, k):
    #Using recursion; Space O(n)
    if node == None:
        return 0
    index = kthToLast(node.next, k) + 1
    if index == k:
        print(node.data)
    return index

n = Node(4)
insertNode(n, 8)
insertNode(n, 1)
insertNode(n, 1)
insertNode(n, 5)
insertNode(n, 9)
printLL(n)
print()
kthToLast(n, 5)

