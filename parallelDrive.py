from parallelGolca import parallelGameOfLife
from golca2 import *
from golca3 import *
from golca4 import *
def genericDriver():
    try:
        str1 = "Enter 1 for general linear algebra test,\n 2 for special linear"
        str2 = " algebra test,\n 3 for orthogonal algebra test,\n and 4 for"
        str3 = " symplectic algebra test! "
        p = int(input(str1+str2+str3))
    except: return
    if p <= 0 and p>=5:
        print("Sorry! Please try again later!")
        return
    else:
        try: n = int(input("Enter the size of the grid! "))
        except: return
        if p == 1: grid, backEnd = createGLgrid(n)
        elif p == 2: grid, backEnd = createSLgrid(n)
        elif p == 3: grid, backEnd = createSOgrid(n)
        elif p == 4: grid, backEnd = createSPgrid(n)
        t = int(input("Enter the number of steps! "))
        parallelGameOfLife(grid,backEnd,t)
        r1 = checkSLgrid(grid)
        r2 = checkSOgrid(grid)
        r3 = checkSPgrid(grid)
        if p == 1: print("Initially the grid is of general linear algebra.")
        elif p == 2: print("Initially the grid is of special linear algebra.")
        elif p == 3: print("Initially the grid is of orthogonal algebra.")
        elif p == 4: print("Initially the grid is of symplectic algebra.")
        if r3: print("Finally the grid is of symplectic algebra!")
        elif r2: print("Finally the grid is of orthogonal algebra!")
        elif r1: print("Finally the grid is of special linear algebra!")
        else: print("Finally the grid is of general linear algebra!")

while True:
    genericDriver()
    try:
        msg = input("Do you want to continue? ").lower()
    except: break
    if msg != 'yes': break