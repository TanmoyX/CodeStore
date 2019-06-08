s1 = 'pathn'
s2 = 'ntpah'

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    count_arr = [0] * 256
    for i in range(len(s1)):
        count_arr[ord(s1[i])] += 1
        count_arr[ord(s2[i])] -= 1
    for i in count_arr:
        if i != 0:
            return False
    return True

print(checkPermutation(s1, s2))
