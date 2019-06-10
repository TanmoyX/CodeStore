string1 = 'abcdklmeefghij'
string2 = 'abcdefghij'

def unique(string):
    L = list(string)
    L.sort()
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            return False
    return True
        

print(unique(string1))
print(unique(string2))
