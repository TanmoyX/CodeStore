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

def removeDuplicates(node):
    #This method has a time complexity of O(N) with temporary buffer
    s = set()
    if node == None:
        return None
    head = node
    while node != None:
        if node.data in s:
            prev.next = node.next
            node = node.next
        else:
            s.add(node.data)
            prev = node
            node = node.next
    return head

n = Node(4)
insertNode(n, 8)
insertNode(n, 1)
insertNode(n, 1)
insertNode(n, 5)
insertNode(n, 9)
printLL(n)
print()
printLL(removeDuplicates(n))

