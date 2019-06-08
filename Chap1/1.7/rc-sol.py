def transpose(arr, R, C):
    for i in range(R):
        for j in range(i, C):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t

def reverseColumns(arr, C):
    for i in range(C):
        j = 0
        k = C - 1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

def reverseRows(arr, R):
    for i in range(R):
        arr[i] = arr[i][::-1]

def printMat(arr, R, C):
    for i in range(R):
        for j in range(C):
            print(str(arr[i][j]), end=" ")
        print()

arr = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

printMat(arr, 4, 4)
print()

#For Anti-Clock 90 degree rotation
transpose(arr, 4, 4)
reverseColumns(arr, 4)
printMat(arr, 4, 4)
print()

#For Clock 90 degree rotation
transpose(arr, 4, 4)
reverseRows(arr, 4)
printMat(arr, 4, 4)


