s1 = 'pathn'
s2 = 'ntpah'

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    if s1 == s2:
        return True
    return False

print(checkPermutation(s1, s2))
