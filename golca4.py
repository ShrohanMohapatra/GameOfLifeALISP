def checkSPgrid(M):
    n = len(M)
    W = [[0 for j in range(n)] for i in range(n)]
    for i in range(int(n/2)):
        for j in range(int(n/2),n):
            W[i][j] = 1
            W[j][i] = 1
    Mt = [[M[j][i] for j in range(n)] for i in range(n)]
    A = [[0 for j in range(n)] for i in range(n)]
    B = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                A[i][j] = (A[i][j]+Mt[i][k]*W[k][j])%2
                B[i][j] = (B[i][j]+W[i][k]*M[k][j])%2
    flag = True
    for i in range(n):
        for j in range(n):
            flag = flag and (A[i][j]+B[i][j])%2 == 0
    return flag