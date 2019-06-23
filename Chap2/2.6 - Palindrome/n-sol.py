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

def checkPalindrome(node):
    head = node
    fast = node
    slow = node
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    if fast != None:
        slow = slow.next
    
    newHeadSecond = revLL(slow)
    
    while newHeadSecond != None:
        if head.data != newHeadSecond.data:
            return False
        head = head.next
        newHeadSecond = newHeadSecond.next
        
    return True
    
def revLL(node):
    p1 = None
    p2 = None
    p3 = node
    
    while p3 != None:
        p1 = p2
        p2 = p3
        p3 = p3.next
        p2.next = p1
    return p2

n = None
n = insertNode(n, 6)
n = insertNode(n, 4)
n = insertNode(n, 3)
n = insertNode(n, 3)
n = insertNode(n, 4)
n = insertNode(n, 6)
printLL(n)
print()
print(checkPalindrome(n))