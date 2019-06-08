def compress(s):
    item = ''
    val = 0
    L = []
    for i in s:
        if i == item:
            val += 1
        else:
            if item == '':
                val += 1
                item = i
            else:
                L.append(item)
                if val > 1:
                    L.append(str(val))
                item = i
                val = 1
    L.append(item)
    if val > 1:
        L.append(str(val))
    print(''.join(L))

compress('aaaabbaacccacb')
compress('abc')
