def oneAway(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        s1,s2 = s2,s1
        l1,l2 = l2, l1
    index1 = 0
    index2 = 0
    L1 = list(s1)
    L2 = list(s2)
    diff = False
    while (index1 < l1 and index2 < l2):
        if L1[index1] != L2[index2]:
            if diff:
                return False
            diff = True
            if l1 == l2:
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True

print(oneAway('ac', 'abc'))
print(oneAway('ac', 'as'))
print(oneAway('ac', 'a'))
print(oneAway('ac', 'avb'))
