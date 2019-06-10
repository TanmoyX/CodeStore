def setZero(mat):
    #Using first_row and first_col as a store for the rest of the matrix
    
    first_row = False
    first_col = False

    #Check if first col has a zero
    for i in range(len(mat)):
        if mat[i][0] == 0:
            first_col = True
            break

    #Check if first row has a zero
    for i in range(len(mat[0])):
        if mat[0][i] == 0:
            first_row = True
            break

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    for i in range(1, len(mat)):
        if mat[i][0] == 0:
            nullifyRow(mat, i)
            
    for i in range(1, len(mat[0])):
        if mat[0][i] == 0:
            nullifyCol(mat, i)

    if first_row:
        nullifyRow(mat, 0)

    if first_col:
        nullifyCol(mat, 0)

def nullifyRow(mat, row):
    for i in range(len(mat[0])):
        mat[row][i] = 0

def nullifyCol(mat, col):
    for i in range(len(mat)):
        mat[i][col] = 0                   

def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = " ")
        print()

matrix = [[1,2,3,4],[0,7,8,5],[4,2,0,1],[1,4,3,1]]
printMat(matrix)
print()
setZero(matrix)
printMat(matrix)
