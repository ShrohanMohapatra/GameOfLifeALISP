from golca import randint
def createGLgrid(n):
    grid = [[randint(0,1) for j in range(n)] for i in range(n)]
    backEnd = [[randint(0,1) for j in range(n)] for i in range(n)]
    return grid, backEnd
def createSLgrid(n):
    grid = [[randint(0,1) for j in range(n)] for i in range(n)]
    backEnd = [[randint(0,1) for j in range(n)] for i in range(n)]
    f = randint(0,int(n/2)) # number of non-zero diagonal values
    for k in range(n): grid[k][k] = 0
    while f>0:
        p = randint(0,n-1)
        if grid[p][p] == 0:
            grid[p][p] = 1
            q = randint(0,n-1)
            while q == p: q = randint(0,n-1)
            grid[q][q] = 1
            f = f - 1
        else: pass
    return grid, backEnd
def createSOgrid(n):
    grid = [[0 for j in range(n)] for i in range(n)]
    backEnd = [[randint(0,1) for j in range(n)] for i in range(n)]
    for k in range(n): grid[k][k] = 0
    for i in range(n):
        for j in range(i+1,n):
            grid[i][j] = randint(0,1)
            grid[j][i] = grid[i][j]
    return grid, backEnd