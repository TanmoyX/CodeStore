def checkPalinPermutation(s):
    odd_count = 0
    count_arr = [0] * 26
    print(count_arr)
    for i in list(s):
        if i >= 'a' and i <= 'z':
            count_arr[ord(i)-ord('a')] += 1
            if count_arr[ord(i)-ord('a')] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
    return odd_count < 2

print(checkPalinPermutation('tact coa'))
