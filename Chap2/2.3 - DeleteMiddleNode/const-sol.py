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

def deleteMiddleNode(node):
    if node == None or node.next == None:
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True

n = Node(4)
insertNode(n, 8)
insertNode(n, 1)
insertNode(n, 1)
insertNode(n, 5)
insertNode(n, 9)
printLL(n)
print()
deleteMiddleNode(n.next)
printLL(n)
