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
    stack1 = []
    stack2 = []
    carry = 0
    
    while n1 != None:
        stack1.append(n1.data)
        n1 = n1.next
        
    while n2 != None:
        stack2.append(n2.data)
        n2 = n2.next

    while stack1 != [] or stack2 != []:
        val1 = stack1.pop(len(stack1) - 1)
        val2 = stack2.pop(len(stack2) - 1)
        val = val1 + val2 + carry
        
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
    
    while stack1 != []:
        val1 = stack1.pop(len(stack1) - 1)
        val = val1 + carry
        
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
            
    while stack2 != []:
        val2 = stack2.pop(len(stack2) - 1)
        val = val1 + carry
        
        if val <= 9:
            resLL = insertNode(resLL, val)
            carry = 0
        else:
            resLL = insertNode(resLL, val % 10)
            carry = 1
        
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