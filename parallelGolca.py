from threading import Thread
def newSum(A):
    r = 0
    for k in range(1,len(A)): r = r + A[k]
    return r
liveSurv = lambda A: 1 if A[0]==1 and 2<=newSum(A)<=3 else 0
deadSurv = lambda A: 1 if A[0]==0 and newSum(A)==3 else 0
modThree = lambda k: -1 if k%3 == 2 else k%3
def caUpdate(j,k,n,grid,backEnd):
    neighbor = [0 for l in range(9)]
    for p in range(9):
        neighbor[p] = grid[(j+modThree(int(p/3)))%n][(k+modThree(p))%n]
    if neighbor[0] == 1: backEnd[j][k] = liveSurv(neighbor)
    elif neighbor[0] == 0: backEnd[j][k] = deadSurv(neighbor)
def caRelax(j,k,n,grid,backEnd):
    grid[j][k] = backEnd[j][k]
def parallelGameOfLife(grid,backEnd,step):
    n = len(grid)
    for i in range(step):
        threadUpdate = [
            [Thread(target=caUpdate,args=(j,k,n,grid,backEnd)) for k in range(n)]
            for j in range(n)
            ]
        for j in range(n):
            for k in range(n): threadUpdate[j][k].start()
        for j in range(n):
            for k in range(n): threadUpdate[j][k].join()
        threadRelax = [
            [Thread(target=caRelax,args=(j,k,n,grid,backEnd)) for k in range(n)]
            for j in range(n)
            ]
        for j in range(n):
            for k in range(n): threadRelax[j][k].start()
        for j in range(n):
            for k in range(n): threadRelax[j][k].join()