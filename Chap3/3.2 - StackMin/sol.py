class Stack:
    def __init__(self):
        self.L = []
        self.L1 = []
        
    def push(self, val):
        if val <= self.peek(self.L):
            self.L1.append(val)
        self.L.append(val)
        
    def peek(self, arr):
        if arr == []:
            return 99999
        else:
            return arr[len(arr) - 1]
    
    def pop(self):
        val = self.L.pop()
        if val == self.peek(self.L1):
            return self.L1.pop()
        else:
            return val
    
    
        
