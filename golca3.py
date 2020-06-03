from random import randint
def createSPgrid(n):
    A = [[randint(0,1) for j in range(n)] for i in range(n)]
    backEnd = [[randint(0,1) for j in range(2*n)] for i in range(2*n)]
    B = [[2 for j in range(n)] for i in range(n)]
    C = [[2 for j in range(n)] for i in range(n)]
    for k in range(n): B[k][k] = randint(0,1)
    for i in range(n):
        for j in range(i+1,n):
            B[i][j] = randint(0,1)
            B[j][i] = B[i][j]
    for k in range(n): C[k][k] = randint(0,1)
    for i in range(n):
        for j in range(i+1,n):
            C[i][j] = randint(0,1)
            C[j][i] = C[i][j]
    grid = [[5 for j in range(2*n)] for i in range(2*n)]
    for i in range(2*n):
        for j in range(2*n):
            if i<n and j<n: grid[i][j] = A[i][j]
            elif i<n and j>=n: grid[i][j] = B[i][j-n]
            elif i>=n and j<n: grid[i][j] = C[i-n][j]
            else: grid[i][j] = A[j-n][i-n]
    return grid, backEnd
def checkSLgrid(A):
    t = 0
    for k in range(len(A)): t = (t + A[k][k])%2
    return t == 0
def checkSOgrid(A):
    flag1, flag2 = True, True
    for k in range(len(A)):
        flag1 = flag1 and A[k][k] == 0
        for m in range(k+1,len(A)):
            flag2 = flag2 and A[k][m] == A[m][k]
    return flag1 and flag2