from random import randint
from pprint import pprint
def newSum(A):
    r = 0
    for k in range(1,len(A)): r = r + A[k]
    return r
liveSurv = lambda A: 1 if A[0]==1 and 2<=newSum(A)<=3 else 0
deadSurv = lambda A: 1 if A[0]==0 and newSum(A)==3 else 0
modThree = lambda k: -1 if k%3 == 2 else k%3
def createGrid(n):
    grid = [[randint(0,1) for j in range(n)] for i in range(n)]
    backEnd = [[randint(0,1) for j in range(n)] for i in range(n)]
    return grid, backEnd
def gameOfLife(grid,backEnd,step):
    neighbor = [0 for l in range(9)]
    n = len(grid)
    for i in range(step):
        for j in range(n):
            for k in range(n):
                for p in range(9):
                    neighbor[p] = grid[(j+modThree(int(p/3)))%n][(k+modThree(p))%n]
                if neighbor[0] == 1: backEnd[j][k] = liveSurv(neighbor)
                elif neighbor[0] == 0: backEnd[j][k] = deadSurv(neighbor)
        for j in range(n):
            for k in range(n): grid[j][k] = backEnd[j][k]
def driver():
    d = int(input("Enter the size of grid. "))
    grid, backEnd = createGrid(d)
    print("The initial state of the grid")
    pprint(grid)
    n = int(input("Enter the number of steps. "))
    gameOfLife(grid, backEnd, n)
    pprint(grid)
# driver()