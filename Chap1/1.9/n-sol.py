def isSubstring(s1, s2):
    #A superb solution. If you add the rotated string to itself it will have a full entire string in the middle. Just check for it then
    check = s2 + s2
    if s1 in check:
        return True
    else:
        return False

print(isSubstring('tanmoy', 'nmoyta'))
