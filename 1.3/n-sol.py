def replaceSpace(s):
    space_count = 0
    s = list(s)
    print(s)
    for i in s:
        #Count spaces
        if i == ' ':
            space_count += 1
    n = len(s)
    MAX = n
    while s[n-1] == ' ':
        #Removing trailing space count
        space_count -= 1
        n -= 1

    #Calculating new length
    new_length = n + space_count * 2
    if new_length > MAX:
        return -1

    index = new_length - 1
    
    for i in range(n-1,0,-1):
        #Traversing string from the end to perform inplace replacement
        print(s[i], index)
        if (s[i] == ' '):
            s[index] = '0'
            s[index - 1] = '2'
            s[index - 2] = '%'
            index = index - 3
        else:
            s[index] = s[i]
            index -= 1
    print(''.join(s))

replaceSpace('Mr John Smith    ')
