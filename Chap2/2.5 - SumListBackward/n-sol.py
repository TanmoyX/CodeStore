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

def findSumLL(n1, n2):
    resLL = None
    carry = 0
    while n1 != None or n2 != None:
        val = (n1.data + n2.data + carry)
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
        n1 = n1.next
        n2 = n2.next
        
    while n1 != None:
        val = n1.data + carry
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
        n1 = n1.next
        
    while n2 != None:
        val = n2.data + carry
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
        n2 = n2.next
    
    if carry != 0:
        resLL = insertNode(resLL, carry)
                
    return resLL

n1 = None
n1 = insertNode(n1, 7)
n1 = insertNode(n1, 1)
n1 = insertNode(n1, 6)
printLL(n1)
print()
n2 = None
n2 = insertNode(n2, 2)
n2 = insertNode(n2, 9)
n2 = insertNode(n2, 5)
printLL(n2)
print()
printLL(findSumLL(n1,n2))
